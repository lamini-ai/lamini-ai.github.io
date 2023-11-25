# Dataset Augmenters

Generate large and diverse datasets from as few as tens of examples with our dataset augmenters! Here is an example of how to do so:

```python
from llama.tools.augmenters import augment, augment_with_answers, augment_question_answer_pairs

# Input
class Question(Type):
    question: str = Context("a question")

# Output
class Answer(Type):
    answer: str = Context("a response to question")

seed_data = [[Question(question='What is Lamini?'), Answer(answer='Lamini is the LLM platform for every developer to build customized, private models: easier, faster, and better-performing than any general purpose LLM..')], ...]

# augment seed dataset with questions
augmented_questions = augment(seed_data, n=10, model_name='lamini/open') # returns a list of 10 new questions based on your seed data!

# augment seed dataset with answers
augmented_answers = augment_with_answers(augmented_questions, output_type=Answer, model_name='lamini/instruct') # returns a list of answers for each new question

# augment seed dataset with question/answer pairs
augmented_question_answer_pairs = augment_question_answer_pairs(seed_data, n=10, question_model_name='lamini/open', answer_model_name='lamini/instruct') # returns a list of 10 new question/answer tuples based on your seed data!
```
