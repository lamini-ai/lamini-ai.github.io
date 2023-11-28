Efficiency matters: and sometimes you don't have to train the entire model to get the performance you need.

Enter PEFT: parameter-efficient finetuning. In combination with a few techniques, we train LoRAs (low-rank adapters) on top of a pretrained LLM to get the same performance as finetuning the entire model, but with 266x fewer parameters and 1.09 billion times faster model switching.

All you have to do to enable training LoRAs (efficient finetuning) is to set the `enable_peft` flag to `True` when instantiating your model.

```python hl_lines="1"
llm = LlamaV2Runner(enable_peft=True)
llm.load_data(data)
llm.train()
llm.evaluate()
```

That's it! 🎉 So speedy to get speed :)
