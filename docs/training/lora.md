Efficiency matters: and sometimes you don't have to train the entire model to get the performance you need.

Enter PEFT: parameter-efficient finetuning. In combination with a few techniques, we train LoRAs (low-rank adapters) on top of a pretrained LLM to get the same performance as finetuning the entire model, but with 266x fewer parameters and 1.09 billion times faster model switching.

This efficiency gain is on and handled by default so you can use the correct model.

```python hl_lines="1"
llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
llm.data = data
llm.train()
llm.evaluate()
```

That's it! 🎉 So speedy to get speed :)

<br><br>
