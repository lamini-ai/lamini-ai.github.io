# Walkthrough Example

## Import Llama and initialize an LLM engine

```python
from llama import LLM

llm = LLM(name="marketing")
```

## Define the LLM interface

Define the input and output types. Be sure to include the `Context`. This helps
the LLM understand your types in natural language.

```python
from llama import Type, Context

class AdAspects(Type):
  tone: str = Context("tone of the marketing copy")
  product_features: list = Context("product features to promote")
  audience: str = Context("target audience for the message")
  subject: str = Context("subject or topic of the message")
  goal: str = Context("goal of this marketing campaign and message")

class AdCopy(Type):
  title: str = Context("google ad title tag")
  description: str = Context("google ad description")
  keywords: list = Context("keywords for the search engine")
```

## Run the LLM

### Generate ad copy from different aspects you want
```python
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

print(f"Ad copy: {ad_copy}")
```

_Output:_
```sh
> title='Delicious Asian Meals Without Going to a Restaurant | Omsom'
  description="Try Omsom's delicious Asian sauces, aromatics, and home-cooked seasonings and meal packs. Easily cook delicious meals at home for your family."
  keywords=[
    'Asian sauces',
    'Aromatics',
    'Home-cooked seasonings',
    'Meal packs',
    'Delicious meals',
    'Suburban families',
    'Omsom'
    ]
```

### Extract ad aspects from the copy you already have

```python
ad_copy = AdCopy(
    title="Omsom | Proud, loud Asian home cooking",
    description="An Omsom starter is a pantry shortcut for a specific Asian dish, combining all the sauces, aromatics, and seasonings you need.",
    keywords=[
        "asian sauces",
        "asian food",
        "home-cooked asian meals",
        "home-cooked seasonings",
        "at home"
    ]
)

ad_aspects = llm(input=ad_copy, output_type=AdAspects)

print(f"Ad aspects: {ad_aspects}")
```

_Output:_
```sh
> tone='Exciting and proud'
  product_features=[
    'Ready-made sauces and seasonings',
    'Variety of Asian dishes',
    'Easy to use'
    ]
  audience='Home cooks looking for an easy way to make Asian dishes'
  subject='Proud, loud Asian home cooking'
  goal="To encourage home cooks to try out Asian dishes with the help of Omsom's ready-made sauces and seasonings."
```

## Improve the LLM with feedback

```python
llm.improve(on="keywords", to="cite specific {product_features}")

ad_copy = llm(input=aspects, output_type=AdCopy)

print(f"Ad copy after improving: {ad_copy}")
```

_Output:_
```sh
> Ad copy after improving:
  title='Delicious Asian Meals From Omsom 🍱'
  description="Try Omsom's delicious Asian sauces, aromatics, and home-cooked seasonings and meal packs. Easily cook delicious meals at home for your family. 🍲"
  keywords=[
    'Asian sauces',
    'Aromatics',
    'Home-cooked seasonings',
    'Meal packs',
    'Delicious meals',
    'Suburban families',
    'Omsom',
    'Emojis',
    'Gluten-free',
    'Vegan-friendly',
    'Low-sodium',
    'No-MSG'
  ]
```

## Train the LLM on your data

```python
# In the format of [[AdAspects, AdCopy], [AdAspects, AdCopy], ...]
data = get_my_marketing_data()

llm.add_data(data)

ad_copy = llm(input=aspects, output_type=AdCopy)

print(f"Ad copy after adding data: {ad_copy}")
```


<details>
  <summary>Code for <code>get_my_marketing_data()</code></summary>


```python
def get_my_marketing_data():
    return [
    [
    AdAspects(
        tone='Exciting and modern',
        product_features=['Made from oak', 'Variety of meats and cheeses', 'Perfect for entertaining'],
        audience='Home chefs and entertainers',
        subject='Elevate your entertaining with charcuterie boards',
        goal='To showcase the versatility and convenience of charcuterie boards as an entertaining option.',
    ),
    AdCopy(
        title='🧀 Charcuterie Boards Made from Oak | Boardsy',
        description='Get the perfect charcuterie board made from oak for your next gathering. Our key product feature is charcuterie boards made from oak. Shop now with Brand Name.',
        keywords=['charcuterie boards', 'oak', 'key product feature'],
    ),
    ],
    [
    AdAspects(
        tone='Celebratory',
        product_features=['Anniversary messages', 'Customizable messages', 'Personalized messages'],
        audience='Couples celebrating anniversaries',
        subject='Celebrate Your Anniversary with a Special Message',
        goal='To encourage couples to celebrate their anniversaries with a special message.',
    ),
    AdCopy(
        title='🎉 Anniversary Messages - Key Product Feature 🎉 | Hollamark',
        description='Celebrate your special day with our key product feature - anniversary messages. Send heartfelt wishes to your loved ones with our unique and personalized messages from Brand Name.',
        keywords=['anniversary messages', 'key product feature', 'personalized messages', 'heartfelt wishes'],
    ),
    ],
    [
    AdAspects(
        tone='Exciting and enthusiastic',
        product_features=['Unique flavor combinations', 'All-natural ingredients', 'Hand-crafted in small batches'],
        audience='Home cooks and foodies',
        subject='Unlocking the flavors of the world',
        goal='To introduce customers to the unique flavor combinations of artisanal spice blends and encourage them to explore new culinary experiences.',
    ),
    AdCopy(
        title='🌶️ Artisanal Spices - Spice Blends Key Product Feature 🌶️ | Shop Now with Artisanal Spices!',
        description='Discover the unique flavors of artisanal spice blends with our key product feature. Shop now with Artisanal Spices! 🛒',
        keywords=['artisanal spices', 'artisanal spice blends', 'key product feature', 'unique flavors', 'shop now', 'emojis'],
    ),
    ],
    [
    AdAspects(
        tone='Exciting and energetic',
        product_features=['Comfort', 'Durability', 'Breathability', 'Stylish design'],
        audience='Active women',
        subject='Look and feel your best with yoga pants',
        goal='To promote the benefits of yoga pants and encourage active women to purchase them.',
    ),
    AdCopy(
        title='🧘‍♀️ Zennn Yoga Pants - Key Product Feature 🧘‍♀️',
        description='Get the perfect fit and feel with Zennn\'s key product feature - yoga pants. Shop now for the best selection and prices.',
        keywords=['yoga pants', 'key product feature', 'perfect fit', 'best selection', 'best prices'],
    ),
    ],
    [
    AdAspects(
        tone='Exciting and informative',
        product_features=['Perfect recipes for keto dieters', 'Easy to follow instructions', 'Nutritional information for each recipe'],
        audience='Keto dieters looking for meal ideas',
        subject='Delicious Keto Recipes',
        goal='To promote the key product feature of perfect recipes, keto and encourage keto dieters to try the recipes.',
    ),
    AdCopy(
        title='🍽 Perfect Recipes for Keto Dieters - Key Product Feature 🥗 | Saladmania',
        description='Get the perfect recipes for your keto diet with our key product feature. Enjoy delicious meals and stay on track with your diet. 🍽 | Brand Name',
        keywords=['perfect recipes', 'keto diet', 'key product feature', 'delicious meals'],
    ),
    ],
    [
    AdAspects(
        tone='Fun and exciting',
        product_features=['Unique flavors', 'Variety of toppings', 'Customizable options'],
        audience='Young adults and families',
        subject='Enjoy delicious ice cream at the microcreamery',
        goal='To increase awareness of the microcreamery and encourage customers to visit and try the unique flavors and toppings.',
    ),
    AdCopy(
        title='🍦 Delicious Ice Cream from Microcreamery - Key Product Feature 🍦',
        description='Enjoy delicious ice cream from Microcreamery, with a key product feature that sets it apart from the competition. 🍦',
        keywords=['ice cream, microcreamery, key product feature, delicious, emojis, Microcreamery, brand name'],
    ),
    ],
    [
    AdAspects(
        tone='Exciting and Innovative',
        product_features=['Easy to use interface', 'Comprehensive data tracking', 'Automated reporting', 'Customizable settings'],
        audience='Ohio-based software developers',
        subject='Unlocking the Potential of Ohio Statewide Software Leagues',
        goal='To showcase the features of Ohio statewide software leagues and demonstrate how they can help software developers maximize their potential.',
    ),
    AdCopy(
        title='🎮 Ohio Statewide Software Leagues - Key Product Feature | Ohio Statewide',
        description='Get the most out of your software with Ohio Statewide Software Leagues. Our key product feature is designed to help you 🚀 maximize your software\'s potential. | Ohio Statewide',
        keywords=['Ohio Statewide Software Leagues', 'Key Product Feature', 'Software Leagues', 'Maximize Software Potential', 'Ohio Statewide'],
    ),
    ],
    [
    AdAspects(
        tone='Inspirational',
        product_features=['Variety of scripts', 'Professional guidance', 'Access to industry professionals'],
        audience='Actors and actresses',
        subject='Unlocking Your Potential as an Actor or Actress',
        goal='To inspire and motivate actors and actresses to reach their full potential through practice theater scripts.',
    ),
    AdCopy(
        title='🎭 Practice Theater Scripts for Actors & Actresses by Brand Name 🎭',
        description='Get the best 🎭 practice theater scripts for actors and actresses from Brand Name. Improve your performance with our selection of scripts.',
        keywords=['practice theater scripts', 'theater scripts for actors', 'theater scripts for actresses', 'improve performance', 'theater scripts'],
    ),
    ],
    [
    AdAspects(
        tone='Inspirational',
        product_features=['High intensity interval training', 'Strength training', 'Cardio workouts', 'Nutrition advice'],
        audience='Men aged 18-35',
        subject='Get Fit and Healthy with Mens Health Workouts',
        goal='To inspire men to take control of their health and fitness through mens health workouts.',
    ),
    AdCopy(
        title='💪 Mens Health Workouts - Get Fit Now! | Mens Health',
        description='Get fit now with Mens Health Workouts. Get the best results with our tailored programs and expert advice. | Mens Health',
        keywords=['mens health workouts', 'fitness', 'exercise', 'get fit', 'mens health'],
    ),
    ],
    [
    AdAspects(
        tone='Informative and helpful',
        product_features=['Easy to use', 'Accurate calculations', 'Comprehensive loan comparison', 'Customizable repayment plans'],
        audience='College students and recent graduates',
        subject='Student loan calculators',
        goal='To inform college students and recent graduates of the benefits of using student loan calculators to compare and customize their loan repayment plans.',
    ),
    AdCopy(
        title='🤓 ABC Financial - Get the Best Student Loan Calculators 🤓',
        description='Get the best student loan calculators from ABC Financial to help you manage your finances. Our key product feature helps you make the right decisions. 🤓',
        keywords=['student loan calculators', 'ABC Financial', 'key product feature', 'student loan calculator', 'loan calculator', 'student loan repayment calculator', 'student loan repayment'],
    ),
    ],
]
```
</details>


_Output:_
```sh
> Ad copy after adding data:
  title='🥢 Delicious Asian Meals at Home with Omsom - Key Product Feature 🥢 | Omsom'
  description="Get delicious Asian meals at home with Omsom's key product feature. Enjoy the flavors of Asia without going to a restaurant. 🥢 | Omsom"
  keywords=[
    'Asian meals',
    'Key product feature',
    'Asian sauces',
    'Aromatics',
    'Home-cooked seasonings',
    'Meal packs',
    'Omsom',
  ]
```

## More advanced training

Coming soon to the docs :)

## Additional examples in public notebooks

- [Marketing Copy Generation in Google Colab](https://colab.research.google.com/drive/1Ij5xATu0DDtQNimvhzxyP--ttPO-TFES)

- [Tweet Generation in Google Colab](https://powerml.co/tweet)
