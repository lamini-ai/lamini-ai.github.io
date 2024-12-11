# Classifier Agent Toolkit

The Lamini Classifier Agent Toolkit (CAT) allows you to create and refine a key building block for agentic systems: classifiers that can quickly categorize a large number of text inputs across any number of pre-defined categories.

You can use CAT via Lamini's [REST API](../api.md), [Python SDK](../lamini_python_class/lamini.md#laminiclassifylamini_classifier), or through the web interface.

## What makes CAT different?

- Accuracy for many classes: >99% accuracy on evals even with >500 classes
- High throughput: process 100k tokens/s
- Consistent latency: sub-2s latency even when classifying thousands of inputs with hundreds of classes
- Confidence scores: for more accurate workflows
- Built for iteration: get metrics and output evals for any model, and even compare models to measure progress

## Working with CAT

1. Create a project
    1. Define your classes
    1. Provide initial examples (you can get high accuracy with just 3 examples per class)
1. Train your first model version (takes about 1 minute per class)
1. Use the classifier
    1. Provide an input, get back all the classes and the confidence score for each
1. Run eval to see metrics (if you're happy with the results, you can use the model immediately - no deployment or other step required)
1. Add examples to improve performance
1. Train a new model version
1. Run eval to compare your new version to the first one
1. Repeat to keep improving

Check out our examples repo for a notebook with sample code for this entire workflow: [Classifier Agent Toolkit](https://github.com/lamini-ai/lamini-examples/blob/main/classify/classify.ipynb)

## Best Practices

1. **Start Small**: Start with just a few (3-5) examples per class
1. **Variety**: Provide diverse, representative examples for each class
1. **Class Balance**: Try to maintain a similar number of examples per class
1. **Validation**: Test your classifier with various inputs
