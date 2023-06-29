# Question Answer Model

In this walkthrough, we'll build a working question answer model to demonstrate how one might use Lamini to gain quick insight into a specialized topic. Here, we've specialized this walkthrough to target our company blog.

## Import the LLM engine from the llama module

```python
from llama import LLMEngine

llm = LLMEngine(id="QA")
```

## Define the LLM interface

Define the input and output types. Be sure to include the `Context`. This helps
the LLM understand your types in natural language.

In this example, the input is a question about Lamini, and the output is the answer.

```python
from llama import Type, Context

# Input
class Question(Type):
    question: str = Context("A question")


# Output
class Answer(Type):
    answer: str = Context("An answer to the question")

```

A general LLM will not have any information about our company, but we can also pass our own data (more on that below) for it to learn from! Let's add a type for that as well:

```python

# Data
class Document(Type):
    text: str = Context("A document")
```

## Add documentation to the model for retrieval

In this next step, we can pass our blogpost as a list of `Document` objects into the model. Then we can call the model.

```python
data = get_documentation()

llm.save_data(data)

question = Question(question='What is Lamini?')

answer = llm(input=question, output_type=Answer)

print(f"Response:\n {answer.answer}")
```

<details>
  <summary>Code for <code>get_documentation()</code> </summary>

```python
def get_documentation():
    return [Document(text="""Introducing Lamini, the LLM Engine for Rapidly Customizing Models
    tl;dr:
    Lamini emerges from stealth to give every developer the superpowers that took the world from GPT-3 to ChatGPT!
    Today, you can try out our hosted data generator for training your own LLMs, weights and all, without spinning up any GPUs, in just a few lines of code from the Lamini library.
    You can play with an open-source LLM, trained on generated data using Lamini.
    Sign up for early access to our full LLM training module, including enterprise features like virtual private cloud (VPC) deployments.
    Training LLMs should be as easy as prompt-tuning 🦾
    Why is writing a prompt so easy, but training an LLM from a base model still so hard? Iteration cycles for fine-tuning on modest datasets are measured in months because it takes significant time to figure out why fine-tuned models fail. Conversely, prompt-tuning iterations are on the order of seconds, but performance plateaus in a matter of hours. Only a limited amount of data can be crammed into the prompt, not the terabytes of data in a warehouse.

    It took OpenAI months with an incredible ML team to fine-tune and run RLHF on their base GPT-3 model that was available for years — creating what became ChatGPT. This training process is only accessible to large ML teams, often with PhDs in AI.

    Technical leaders at Fortune 500 companies have told us:
    "Our team of 10 machine learning engineers hit the OpenAI fine-tuning API, but our model got worse — help!"
    "I don’t know how to make the best use of my data — I’ve exhausted all the prompt magic we can summon from tutorials online."

    That’s why we’re building Lamini: to give every developer the superpowers that took the world from GPT-3 to ChatGPT.
    Rapidly train LLMs from any base model
    Lamini is an LLM engine that allows any developer, not just machine learning experts, to train high-performing LLMs, as good as ChatGPT, on large datasets with just a few lines of code from the Lamini library (check out an example here!)

    The optimizations in this library reach far beyond what’s available to developers now, from more challenging optimizations like RLHF to simpler ones like reducing hallucinations.
    Lamini makes it easy to run multiple base model comparisons in just a single line of code, from OpenAI’s models to open-source ones on HuggingFace.

    Now that you know a bit about where we’re going: today, we’re excited to release our first major community resource!
    Available now: a hosted data generator for LLM training
    We are excited to release several important steps to training your own LLM:
    The Lamini library for optimized prompt-tuning and typed outputs (try our playground to see it now).
    The advanced Lamini library for fine-tuning and RLHF, in just a few lines of code (sign up for early access).
    The first ever hosted data generator for creating data needed to train instruction-following LLMs, licensed for commercial use (all yours, you own it!).
    Open-source instruction-following LLM, using the above tools with only a few lines of code (play with it).
    Steps to a ChatGPT-like LLM for your use case
    Base models have a good understanding of English for consumer use cases. But when you need them to learn your vertical-specific language and guidelines, prompt-tuning is often not enough and you will need to build your own LLM.

    Here are the steps to get an LLM that follows instructions to handle your use case like ChatGPT:
    0. Try prompt-tuning ChatGPT or another model. You can use Lamini library’s APIs to quickly prompt-tune across different models, swapping between OpenAI and open-source models in just one line of code. We optimize the right prompt for you, so you can take advantage of different models without worrying about how to format the prompt for each model.

    1. Build a large dataset of input-output pairs. These will show your model how it should respond to its inputs, whether that's following instructions given in English, or responding in JSON. Today, we’re releasing a repo to generate 50k data points from as few as 100 data points, using the Lamini library to hit the Lamini engine, so you don’t have to spin up any GPUs. We include an open-source 50k dataset in the repo. (More details below on how you can do this!)

    2. Fine-tune a base model on your large dataset. Alongside the data generator, we’re also releasing an LLM that is fine-tuned on the generated data using Lamini. We’ll soon be releasing the ability to do this programmatically. You can also hit OpenAI’s fine-tuning API as a great starting point.

    3. Run RLHF on your fine-tuned model. With Lamini, you no longer need a large ML and human labeling team to run RLHF.

    4. Deploy to your cloud. Simply hit the API endpoint in your product or feature.

    Lamini delivers the ease of prompt-tuning, with the performance of RLHF and fine-tuning. It will soon handle this entire process (sign up for early access!).
    Deeper dive into step #1: a ChatGPT-like data generator
    ChatGPT took the world by storm because it could follow instructions from the user, while the base model that it was trained from (GPT-3) couldn’t do that consistently. For example, if you asked the base model a question, it might generate another question instead of answering it.

    For your application, you might want similar "instruction-following" data, but you could also want something completely different, like responding only in JSON.

    You'll need a dataset of ~50k instruction-following examples to start. Don't panic. You can now use Lamini’s data generator on Github to turn just 100 examples into over 50k in just a few lines of code.

    You don’t need to spin up any GPUs, because Lamini hosts it for you. All the data that is used is commercial-use-friendly, meaning you own all the data that comes out of it.

    You can customize the initial 100+ instructions so that the LLM follows instructions in your own vertical. Once you have those, submit them to the Lamini data generator, and voilà: you get a large instruction-following dataset on your use case as a result!
    The Lamini data generator is a pipeline of LLMs that takes your original small set of 100+ instructions, paired with the expected responses, to generate 50k+ new pairs, inspired by Stanford Alpaca. This generation pipeline uses the Lamini library to define and call LLMs to generate different, yet similar, pairs of instructions and responses. Trained on this data, your LLM will improve to follow these instructions.

    We provide a good default for the generation pipeline that uses open-source LLMs, which we call Lamini Open and Lamini Instruct. With new LLMs being released each day, we update the defaults to the best-performing models. As of this release, we are using EleutherAI’s Pythia for Lamini Open and Databricks’ Dolly for Lamini Instruct. Lamini Open generates more instructions, and Lamini Instruct generates paired responses to those instructions. The final generated dataset is available for your free commercial use (CC-BY license).

    The Lamini library allows you to swap our defaults for other open-source or OpenAI models in just one line of code. Note that while we find OpenAI models to perform better on average, their license restricts commercial use of generated data for training models similar to ChatGPT.

    If you’re interested in more details on how our data generator works, read more or run it here.
    Releasing step #2: open-source LLM, fine-tuned on generated data from step #1
    Some of the generated data is good, some not. Before fine-tuning, the next step is to filter the generated data to mostly high-quality data (just run this simple script in the same repo). Lamini then creates a custom LLM by training a base model on this filtered, generated dataset.

    We have released an open-source instruction-following LLM (CC-BY license) using Lamini to train the Pythia base model with 37k generated instructions, filtered from 70k. Play with this custom LLM in the playground now.
    Pushing the boundaries of fast & usable generative AI
    We’re excited to dramatically improve the performance of training LLMs and make it easy for engineering teams to train them. These two frontiers are intertwined: with faster, more effective iteration cycles, more people will be able to build these models, beyond just fiddling with prompts. We exist to help any company unlock the power of generative AI by making it easy to put their own data to work.

    Team++: We are growing our team with people who are passionate about making it possible to build LLMs 10x faster and making them widely accessible to empower new, extraordinary use cases. If that’s you, please send your resume and a note to careers@lamini.ai. 🤝
    """), Document(text="""How is this different than just using a single provider’s (e.g. OpenAI’s) APIs off the shelf?

    3 major reasons from our customers:
    ‍
    1. Data: Use all of your data, rather than what fits into a prompt.
    2. Ownership: Own the generative AI you build, rather than give your usage and development data to an external party.
    3. Control (cost, latency, throughput): With ownership, you also have more control over the (much lower) cost and (much lower) latency of the model. We expose these controls in an easy interface for your engineering team to customize.
    What does the LLM engine do?

    Our engine runs and optimizes your LLM.

    It brings several of the latest technologies and research to bear that was able to make ChatGPT from GPT-3, as well as Github Copilot from Codex.

    These include, among others, fine-tuning, RLHF, information retrieval specialized for LLMs, and GPU optimization.
    What LLMs is the LLM engine using under the hood?

    We build on the latest generation of models to make your LLM perform best. We work with customers to determine which models are appropriate, depending on your specific use cases and data constraints.

    For example, using OpenAI’s well-known GPT-3 and ChatGPT models are a great starting point for some customers, but not others. We believe in following your needs, and using the best models for you.
    Do you build my own large model?

    Yes, the resulting model is very large!

    However, what’s exciting is that it builds on the great work before it, such as GPT-3 or ChatGPT. These general purpose models know English and can answer in the general vicinity of your tasks.

    We take it to the next level to teach it to understand your company’s language and specific use cases, by using your data.

    This means it will do better than a general purpose model on tasks that matter to you, but it won’t be as good as a general purpose model on generic tasks without any data, e.g. putting together a grocery list (unless that’s what your company does).
    If I want to export the model and run it myself, can I do that?

    Yes, we can deploy to any cloud service.* This is on the roadmap with our early customers!

    This includes setup for running our LLM engine in your own environment, e.g. on your AWS/Azure/GCP instances. If you want to, you can export the weights from our engine and you can host the LLM yourself.
    How expensive is using your engine to build and use my model?

    In the range of $5,000 per use case. This highly depends on your usage (frequency of using the model, complexity of the task, amount of data). The costs are associated with compute from the GPU clusters that we use to train the model during development.

    There’s also ongoing cost to run the model after it’s been trained, and that depends on the usage of the model, e.g. from your users, as well as the desired cost and latency you need for your use case.

    We are currently 50% the price of using OpenAI for your own internal development.
    """), Document(text="""Your data.
    Your infra.
    Your LLM.
    Giving every developer the superpowers that took the world from GPT-3 to ChatGPT. Training custom LLMs on your own infrastructure can be as easy as prompt engineering.
    The first LLM engine that can train in your own infrastructure.
    From speed optimizations like LoRA to enterprise features like virtual private cloud (VPC) deployments.
    Beyond prompt-tuning. Beyond fine-tuning.
    Faster training, with optimizations for 10x fewer training iterations, data transformations, and model selection.
    A library any software engineer can use.
    Just a few lines in the Lamini library can train a new LLM. Rapidly ship new versions with an API call. Never worry about hosting or running out of compute.

    Lamini is the world's most powerful LLM engine, unlocking the power of generative AI for every company by putting their data to work.

    """)]
```

</details>

_Output:_

```python
Response:
Lamini is a Python library that provides a simple interface for training and using language models.
```
