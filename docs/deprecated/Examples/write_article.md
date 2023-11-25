# Article Writer Model

In this walkthrough, you'll build an LLM that can write an article from a topic. Feel free to also run the [Colab notebook](https://colab.research.google.com/drive/1ZsKPmXugcIJEJ3SLJ5NyJAxMkyrcF_yN).

## Define the LLM interface

Define the input and output types. Be sure to include the `Context`. This helps
the LLM understand your types in natural language.

```python
from llama import Type, Context

class Input(Type):
    topic : str = Context("what topic the article should cover")

class Output(Type):
    title : str = Context("article title starting, written in markdown, e.g. with #")
    article : str = Context("article body text, written in markdown")
```

## Import the InputOutputRunner from the llama module

```python
from llama import InputOutputRunner

model = InputOutputRunner(input_type=Input, output_type=Output)
```

The Pythia 410M-parameter model is the largest on the free-tier to train for free, and you can specify the model here:

```python
model = InputOutputRunner(input_type=Input, output_type=Output, model_name="EleutherAI/pythia-410m-v0")
```

## Add example data to the model for training

You can import data to this class by using the `save_data` method, which accepts a list of input-output pairs, formatted into your types, above.

```python
data = get_data()
model.load_data_from_paired_lists(data)
```

You can load data in many ways: Pandas DataFrame, CSV, jsonlines, or a list of input-output pairs. See the docs for [InputOutputRunner](/docs/input_output_runner.md) for all the ways.

<details>
  <summary>Code for <code>get_data()</code></summary>

```python
def get_data():
    data = [[{'topic': "birds aren't real"},
  {'title': '"Birds Aren\'t Real: The Shocking Truth"',
   'article': '"Did you know that birds aren\'t actually real? They\'re just a myth perpetuated by society to make us believe in the existence of flying creatures. In reality, birds are just a figment of our imagination, created to make us feel more connected to nature. #BirdsArentReal #MythBusters #FlyingCreatures"'}],
 [{'topic': 'taylor swift as mayor of santa clara (swiftie clara)'},
  {'title': '"Swiftie Clara: Taylor Swift as Mayor of Santa Clara"',
   'article': '"As the world watched in awe, Taylor Swift was sworn in as the new Mayor of Santa Clara. The pop star, known for her catchy tunes and fierce lyrics, has taken on a new role as the leader of the city. But what does this mean for the city and its residents? 🤔🎶"'}],
 [{'topic': 'databricks buys AI startup for $1b'},
  {'title': 'Databricks Buys AI Startup for $1B',
   'article': 'Databricks, a leading provider of data engineering and machine learning platforms, has announced the acquisition of AI startup, AI Startup, for $1 billion. The acquisition is expected to close in the second quarter of this year and will provide Databricks with access to AI Startup\'s cutting-edge technology and talent.\nAccording to a statement released by Databricks, the acquisition will enable the company to expand its offerings and provide customers with a more comprehensive platform for data engineering and machine learning. "With the acquisition of AI Startup, we are further solidifying our position as a leader in the data engineering and machine learning space," said Ali Ghodsi, CEO of Databricks. "We are excited to welcome the talented team from AI Startup to Databricks and look forward to integrating their technology and expertise into our platform."\nAI Startup, which was founded in 2018, has developed a range of AI technologies that are designed to make it easier for developers to build and deploy machine learning models. The startup\'s technology'}],
 [{'topic': 'room-temperature superconductors was replicated'},
  {'title': 'Room-Temperature Superconductors: A New Frontier in Materials Science',
   'article': 'Room-temperature superconductors have long been the holy grail of materials science. For decades, researchers have been working to develop materials that can exhibit superconducting properties at temperatures near or above room temperature (around 20-25°C). While significant progress has been made in recent years, the field has been plagued by a lack of understanding of the underlying mechanisms and the inability to control and manipulate these properties.\nHowever, recent breakthroughs have shown that it is possible to create room-temperature superconducting materials using unconventional methods. These methods involve the use of non-traditional materials and structures, such as topological insulators, and the application of novel techniques, such as strain engineering.\nOne of the most promising approaches to room-temperature superconductivity is the use of topological insulators. These materials have a non-trivial band structure that allows for the formation of Majorana fermions, which are particles that are their own antiparticles. By manipulating the properties of these materials, researchers have been'}],
 [{'topic': 'autonomous vehicles is here while everyone else is buzzing about LLMs and superconductors'},
  {'title': '"The Future of Transportation: How Autonomous Vehicles Are Changing the Game"',
   'article': '"Autonomous vehicles have been making waves in the tech industry, with many companies investing heavily in the development of self-driving cars. But what does the future of transportation look like, and how will autonomous vehicles change the game? In this article, we\'ll explore the benefits and challenges of autonomous vehicles, and how they\'re set to revolutionize the way we travel."'}],
 [{'topic': 'impact of 5G on different industries'},
  {'title': '"The Impact of 5G on Different Industries"',
   'article': '"5G is the latest generation of wireless technology, offering faster speeds and lower latency than its predecessors. This new technology has the potential to transform various industries, from healthcare to manufacturing. In this article, we will explore the impact of 5G on different sectors and how it can revolutionize the way we live and work."'}],
 [{'topic': 'AI and Taiwan and the future of US-China relations'},
  {'title': '"AI and Taiwan: A New Frontier in US-China Relations"',
   'article': '"In the future of US-China Relations, AI will play a crucial role in shaping the dynamics between the two superpowers. Taiwan, with its cutting-edge technology and strategic location, is poised to become a key player in this new frontier. This article will explore the potential implications of AI on US-China relations and how Taiwan can leverage its strengths to become a major player in this emerging field."'}],
 [{'topic': 'renewable energy costs are lower than gas and oil but lobbying keeps big oil around'},
  {'title': 'Renewable Energy Costs Lower Than Gas and Oil, But Lobbying Keeps Big Oil Around',
   'article': 'Renewable energy costs have been steadily decreasing over the past decade, with the cost of solar and wind power dropping by as much as 70% and 50%, respectively. Despite these cost savings, big oil companies continue to lobby against renewable energy sources, using their vast resources to influence government policies and maintain their grip on the industry. According to a recent report by the International Energy Agency (IEA), the cost of renewable energy is now lower than gas and oil in many parts of the world, yet big oil companies are still able to maintain their dominance. This is a clear example of how special interests are able to manipulate the political process to maintain their power and profits, even when it goes against the public interest.'}],
 [{'topic': 'LLMs permeating finance, while compliance is trying to crack down on it'},
  {'title': 'LLMs in Finance: A Growing Concern for Compliance',
   'article': 'LLMs (LLMs) have been increasingly permeating finance, with many firms leveraging their expertise to gain a competitive edge. However, as the use of LLMs becomes more widespread, compliance is struggling to keep up, with regulators scrambling to catch up with the rapidly evolving landscape.\nIn this article, we will explore the growing trend of LLMs in finance, the challenges compliance faces in regulating them, and the potential implications for the industry as a whole.\n# LLMs in Finance: An Overview\nLLMs are advanced degrees that allow lawyers to specialize in a particular area of law. In finance, LLMs are used to provide legal advice and representation to financial institutions, investment firms, and other organizations involved in the financial sector.\narticle: LLMs have become increasingly popular in finance, with many law schools offering specialized programs in financial law. This has led to a surge in the number of lawyers with LLMs in finance, with many firms'}]
]
"""
```
</details>

Now input another topic into the finetuned model.
```python
new_input = Input(topic="AI entertainment just got more popular than netflix")
article = model(new_input)
print(article)
```

See the new article!

_Output:_

````python
Output(
    title="AI-Powered Entertainment: The Future of Entertainment Industry", 
    article="""AI-powered entertainment has been gaining popularity at an unprecedented rate, with some sources suggesting that it may soon surpass Netflix as the most popular form of entertainment. According to a recent survey, 67% of respondents said they would prefer to watch a movie or TV show that uses AI-powered special effects, compared to just 33% who prefer traditional CGI. This shift in consumer preferences has major implications for the entertainment industry, which must now adapt to the changing landscape or risk being left behind.\nIn this article, we will explore the current state of AI-powered entertainment, its potential impact on the industry, and the challenges and opportunities it presents. We will also examine the various ways in which AI is being used to create more immersive and engaging entertainment experiences, and how it is changing the way we consume and interact with media. Whether you're a fan of movies, TV shows, or video games, this article will provide you with a comprehensive overview of the exciting developments happening in the world of AI."""
)
````