# Advanced

Now that you've got the basics, it's time to power up your llama!

## Generate Varied Output

In the [walkthrough example](Examples/playground_example.md), you generated ad copy using the below:

```python
class AdAspects(Type):
  tone: str = Context("tone of the marketing copy")
  product_features: list = Context("product features to promote")
  audience: str = Context("target audience for the message")
  subject: str = Context("subject or topic of the message")
  goal: str = Context("goal of this marketing campaign and message")

class AdCopy(Type):
  h1: str = Context("google ad h1 tag")
  title: str = Context("google ad title tag")
  keywords: list = Context("keywords for the search engine")

aspects = AdAspects(
    tone="bold and bright, but not arrogant",
    product_features=[
        'asian sauces and aromatics',
        'home-cooked seasonings and meal packs that can be easily cooked at home'
    ],
    audience="suburban families",
    subject="delicious asian meals without going to a restaurant",
    goal="get suburban moms and dads to try buy their first omsom pack or free tasting kit"
)

ad_copy = llm(input=aspects, output_type=AdCopy)
```

Running this multiple times should assign the same value to `ad_copy`. But what if you want some variation? That's where `random` comes in! Instead, you can run the below multiple times to get different outputs:

```python
ad_copy = llm(input=aspects, output_type=AdCopy, random=True)
```

## Remove Duplicates

`random` is great for inducing some variety, but what if you want to remove duplicates across copies? You can use `llm.sample` to produce a list of outputs that are all different from each other:

```python
ad_copies = llm.sample(input=aspects, output_type=AdCopy, n=5)
```

You can also use `llm.sample` to ensure variation across attributes within a single copy, for example, making sure that the title and h1 are not the same:

```python
ad_copy = llm.sample(input=aspects, output_type=AdCopy, n=1)[0]
```

## Add Output Scores

Now you can generate varied outputs, but how do you compare between them? You can do so by generating scores! First, update your output type to include the score you wish to generate:

```python
class AdCopy(Type):
  h1: str = Context("google ad h1 tag")
  title: str = Context("google ad title tag")
  keywords: list = Context("keywords for the search engine")
  score: float = Context("score for the ad copy")
```

Then you can run your llm with the given score attribute to have it generate a confidence score for the output:

```python
ad_copy = llm(input=aspects, output_type=AdCopy, random=True, score='score')
```
