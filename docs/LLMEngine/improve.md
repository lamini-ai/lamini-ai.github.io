# llama.LLMEngine.improve

Improves the LLM to produce better output, following your natural language criteria.

```python
llm.improve(on, to)
```

## Parameters

-   on: `str` - attribute in an output's `Type` to improve on
-   to: `str` - natural language description of how to improve the LLM

## Example

```python
llm.improve(on="speed", to="give the average speed, not the max speed")
```
