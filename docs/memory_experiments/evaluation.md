# Evaluating Model Performance

## Overview
This guide walks through the process of evaluating large language models (LLMs) with a focus on real-world impact. Evaluations (evals) ensure your model behaves as expected—so you can iterate and deploy with confidence.

We'll use a customer support chatbot example throughout this guide to demonstrate each step in context.

## Table of Contents
- [What is Eval?](#what-is-eval)
- [Create an Eval Set](#create-an-eval-set)
- [Build an Eval Pipeline](#build-an-eval-pipeline)
- [Run Eval on Base Model](#run-eval-on-base-model)
- [Generate Synthetic Data](#generate-synthetic-data)
- [Run Eval on Tuned Model](#run-eval-on-tuned-model)

## What is Eval?
Evaluations (evals) help you determine whether your model can do a good job in real life. They give you a repeatable way to measure model performance against your expectations.

### Customer Support Example
Let's say you're replacing a rule-based chatbot that frustrates users by saying "I don't know" too often. Your goal is to evaluate if an LLM can give helpful, accurate answers based on your internal help documentation.

Since the real world is complex, start small—just like how you wouldn't train your model on every customer issue at once, you don't need to eval everything upfront either. Start with one core area, like account login issues.

## Create an Eval Set

### Understand Your Objective
What do you want the model to do? What does "correct" mean in your context?

**Example:**
You want the model to answer basic customer questions (e.g., password reset, account deactivation) without escalating to a human rep unnecessarily. Success means fewer users asking for human support.

### Analyze the Problem
What's going wrong now? Where is the existing system failing?

**Example:**  
The current chatbot often gives:
- "Sorry, I don't understand."
- Hallucinated info (e.g., claiming there's a password reset link that doesn't exist)
- Irrelevant answers

Review chat logs to find real examples where the bot failed. Ask:
- Why are users dissatisfied?
- What should a good answer look like?

#### Example Answers

**Bad Answer:**
Q: "How do I reset my password?"
A: "Sorry, I'm not sure. Please contact support."

**Good Answer:**
A: "To reset your password, go to [example.com/reset] and follow the instructions. Let me know if you need help."

Create 20 Questions and Answers
Start with a small, simple eval set—just 20 examples is enough to begin.
Example:
Q: "Can I delete my account?"
A: "Yes, you can delete your account by going to Settings > Account > Delete Account."
Your answers must be accurate—these are your gold answers. The model's job is to match or closely approximate them.

## Build an Eval Pipeline
Now let's automate the evaluation. Human review is slow and subjective. We want a pipeline that can repeatedly and consistently check how well the model is doing.
Eval = Compare Output to Gold Answer
Start by defining: what counts as "correct"?
Customer Support Example:
 You may want to check:
Factuality – Is the answer accurate?
Source alignment – Does it come from your knowledge base?
Semantic similarity – Is it close enough in meaning to the gold answer?
String match – Useful if you're expecting very structured responses.
Example Pipeline for Support Chatbot (Factual QA)
AnswerValidator → Checks if model output matches the gold answer (exact or semantically).
FactValidator → Ensures the answer exists in your customer support docs.
Test the Evaluator Itself
Run the pipeline on your gold set. If your evaluator is wrongly marking good answers as bad (or vice versa), improve the prompt or break the task into smaller validators.

## Run Eval on Base Model
With the pipeline ready, it's time to see how your base model performs.
Customer Support Example:
 You run your base model on the 20-question eval set.
Outcomes:
If it performs well, great! Start adding more complex questions.
If it performs poorly, that's also great—you now know what to improve.
Example Result:
 Out of 20 questions:
5 correct
7 partially correct (missing some info)
8 wrong or hallucinated
Now you know where to focus your training.

## Generate Synthetic Data
Now that you've identified weak spots, it's time to improve your model. A powerful way to do that is to generate synthetic training data based on your eval. With Lamini, you can easily construct an agentic data pipeline with generators and validators that suit your use case and create high quality synthetic data. A guide on generate synthetic data is coming soon too.

## Run Eval on Tuned Model
After training on synthetic data, re-run your eval set to see how your model has improved. Once the model performs well on your eval set, you'll want to go to the next level: more difficult, more complex evaluations.
The majority of the work will be error analysis and iteration—analyzing the eval result, figuring out what the model is not doing well on, adding more training data, or improving your pipelines.







