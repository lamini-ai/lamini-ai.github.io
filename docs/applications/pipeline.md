# LLM Pipeline

Run an LLM on a large amount of data quickly and efficiently.

This pipeline first generates questions from a prompt, then generates answers from the questions.

```python
from lamini.generation.base_prompt_object import PromptObject
from lamini.generation.generation_node import GenerationNode
from lamini.generation.generation_pipeline import GenerationPipeline

class QuestionAnswerPipeline(GenerationPipeline):
    def __init__(self):
        super(QuestionAnswerPipeline, self).__init__()

        self.question_generator = QuestionGenerator(
            "meta-llama/Meta-Llama-3-8B-Instruct", max_new_tokens=200
        )
        self.asnwer_generator = AnswerGenerator(
            "meta-llama/Meta-Llama-3-8B-Instruct", max_new_tokens=100
        )

    def forward(self, x):
        x = self.question_generator(
            x,
            output_type={
                "question_1": "string",
                "question_2": "string",
                "question_3": "string",
            },
        )
        x = self.asnwer_generator(x)
        return x
```

## Data Loading

First, we load the data from a file.

```python
import jsonlines

async def load_earnings_calls():
    path = "<PATH_TO_YOUR_DATA>.jsonl"

    with jsonlines.open(path) as reader:
        for line in reader:
            logger.info(f"Loaded earnings call for {line['ticker']}")
            yield PromptObject(prompt="", data=line)
```

## Question Generation

The question generator generates questions from a prompt.

```python
class QuestionGenerator(GenerationNode):

    def preprocess(self, obj: PromptObject):
        obj.prompt = self.make_prompt(obj)
        logger.info(f"Generating question for {obj.data['ticker']}, {obj.data['q']}")

    def postprocess(self, obj: PromptObject):
        response = obj.response
        questions = [
            response["question_1"],
            response["question_2"],
            response["question_3"],
        ]
        for question in questions:
            ans = PromptObject(prompt=question, data=obj.data.copy())
            yield ans


    def make_prompt(self, obj):
        prompt = (
            "<s>[INSTR]You are a financial analyst with extensive experience at Goldman Sachs."
        )
        prompt += "You are reading the earnings call transcript for the following company:\n\n"
        prompt += "====================\n\n"
        prompt += get_company_info(obj) + "\n"
        prompt += "====================\n\n"
        prompt += (
            "You are reading the following section of the earnings call transcript:\n\n"
        )
        prompt += "====================\n\n"
        prompt += obj.data["transcript"]
        prompt += "====================\n\n"
        prompt += "Consider the numbers in the transscript. "
        prompt += "Ask three questions about the numbers in the transcript that require precise answers. "
        prompt += "Only ask questions that can be answered using the transcript."
        prompt +="[/INSTR]"

        return prompt

```

## Answer Generation

```python
class AnswerGenerator(GenerationNode):

    def postprocess(self, obj: PromptObject):
        logger.info(f"Generated answer for {obj}")

    def preprocess(self, obj: PromptObject):
        obj.data["question"] = obj.prompt
        obj.prompt = self.make_prompt(obj)

    def make_prompt(self, obj: PromptObject):
        prompt = (
            "<s>[INSTR] You are a financial analyst with extensive experience at Goldman Sachs."
        )
        prompt += "You are reading the earnings call transcript for the following company:\n\n"
        prompt += "====================\n\n"
        prompt += get_company_info(obj)
        prompt += "====================\n\n"
        prompt += (
            "You are reading the following section of the earnings call transcript:\n\n"
        )
        prompt += "====================\n\n"
        prompt += obj.data["transcript"] + "\n"
        prompt += "====================\n\n"
        prompt += "Consider the numbers in the transscript. "
        prompt += "If the answer to the question cannot be found in the transcript, reply that you do not know. "
        prompt += "Answer the following questions about the numbers in the transcript. "
        prompt += obj.prompt
        prompt += "[/INSTR]"

        return prompt

```

## Running the Pipeline

This pipeline can be run with the following code:

```python
async def run_pipeline():
    earnings_calls = load_earnings_calls()

    answers = QuestionAnswerPipeline().call(earnings_calls)

    await save_answers(answers)
```

## Saving the Answers

The answers are saved to a file. A progress bar is displayed while saving the answers.

```python
from tqdm import tqdm
import jsonlines

async def save_answers(answers):
    path = "<SAVE_FILE_NAME>.jsonl"

    with jsonlines.open(path, "w") as writer:
        pbar = tqdm(desc="Saving answers", unit=" answers")
        async for answer in answers:
            answer = {
                "ticker": answer.data["ticker"],
                "q": answer.data["q"],
                "date": answer.data["date"],
                "transcript": answer.data["transcript"],
                "prompt": answer.prompt,
                "question": answer.data["question"],
                "answer": answer.response["output"],
            }
            writer.write(answer)
            pbar.update()
```

## Running the Pipeline

The pipeline can be run with the following code:

```python
asyncio.run(run_pipeline())
```

## Chunking the Data

The data is chunked into smaller pieces to fit the model's input size.

```python

def chunk_prompt(obj: PromptObject):
    transcript = obj.data["transcript"]
    chunk_size = 4096
    chunk_step = 2048

    for i in range(0, len(transcript), chunk_step):
        chunk = transcript[i : i + chunk_size]
        chunked_data = obj.data.copy()
        chunked_data["transcript"] = chunk
        prompt_object = PromptObject(prompt=obj.prompt, data=chunked_data)
        yield prompt_object


def get_company_info(obj: PromptObject):
    info = f"Ticker: {obj.data['ticker']}\n"
    info += f"Date: {obj.data['date']}\n"
    info += f"Quarter: {obj.data['q']}\n"
    return info
```
