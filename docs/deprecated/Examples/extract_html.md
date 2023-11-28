# HTML Form Extractor Model

In this walkthrough, you'll build an LLM that can extract HTML form elements. Feel free to also run the [Colab notebook](https://colab.research.google.com/drive/1cn5AaWAsn6oOjz8bbo5JN9m893vmguCh).

## Import the LLM engine from the llama module

```python
from llama import LLMEngine

llm = LLMEngine(id="extract_html", model_name="EleutherAI/pythia-410m-v0") 
```

The Pythia 410M-parameter model is the largest on the free-tier to train for free :)

## Define the LLM interface

Define the input and output types. Be sure to include the `Context`. This helps
the LLM understand your types in natural language.

```python
from llama import Type, Context

class Input(Type):
    html_dom : str = Context("html dom of a form page with first name, last name, and credit card number fields filled out")

class Output(Type):
    first_name : str = Context("first name of the person")
    last_name : str = Context("last name of the person")
    credit_card_number : str = Context("credit card number of the person")

```


## Add example data to the model for training

You can import data to this class by using the `save_data` method, which accepts a list of input-output pairs, formatted into your types, above.

```python
data = get_data()
model.save_data(data)
```

<details>
  <summary>Code for <code>get_data()</code></summary>

```python
def get_data():
    data = [
        [Input(html_dom="""<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form>
        <div>
            <label for="first_name">First Name:</label><br>
            <input type="text" id="first_name" name="first_name" value="John" readonly>
        </div>
        <div>
            <label for="last_name">Last Name:</label><br>
            <input type="text" id="last_name" name="last_name" value="Doe" readonly>
        </div>
        <div>
            <label for="cc_number">Credit Card Number:</label><br>
            <input type="password" id="cc_number" name="cc_number" value="**** **** **** 1234" readonly>
        </div>
        <div>
            <input type="submit" value="Submit">
        </div>
    </form>
</body>
</html>
"""), Output(first_name='John', last_name='Doe', credit_card_number='**** **** **** 1234')],
        [Input(html_dom="""<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form>
        <div>
            <label for="first_name">First Name:</label><br>
            <input type="text" id="first_name" name="first_name" value="Kelly" readonly>
        </div>
        <div>
            <label for="last_name">Last Name:</label><br>
            <input type="text" id="last_name" name="last_name" value="Seegal" readonly>
        </div>
        <div>
            <label for="cc_number">Credit Card Number:</label><br>
            <input type="password" id="cc_number" name="cc_number" value="493929193" readonly>
        </div>
        <div>
            <input type="submit" value="Submit">
        </div>
    </form>
</body>
</html>
"""), Output(first_name='Kelly', last_name='Seegal', credit_card_number='493929193')],
        [Input(html_dom="""<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form>
        <table>
            <tr>
                <td>
                    <label for="full_name">Full Name:</label>
                </td>
                <td>
                    <input type="text" id="full_name" name="full_name" value="Ren Farley" readonly>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="cc_number">Credit Card Number:</label>
                </td>
                <td>
                    <input type="password" id="cc_number" name="cc_number" value="90193990202" readonly>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <input type="submit" value="Submit">
                </td>
            </tr>
        </table>
    </form>
</body>
</html>
"""), Output(first_name='Ren', last_name='Farley', credit_card_number='90193990202')],
        [Input(html_dom="""<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form>
        <div id="personal_details">
            <h3>Personal Details:</h3>
            <label for="full_name">Full Name:</label><br>
            <input type="text" id="full_name" name="full_name" value="Ren Farley" readonly><br>
        </div>
        <div id="credit_card_details">
            <h3>Credit Card Details:</h3>
            <label for="cc_number">Credit Card Number:</label><br>
            <input type="password" id="cc_number" name="cc_number" value="90193990202" readonly><br>
            <label for="expiry_date">Expiry Date:</label><br>
            <input type="text" id="expiry_date" name="expiry_date" placeholder="MM/YY" readonly><br>
        </div>
        <div id="submit_button">
            <input type="submit" value="Submit">
        </div>
    </form>
</body>
</html>
"""), Output(first_name='Ren', last_name='Farley', credit_card_number='90193990202')],
]

    return data
```

</details>


## Train the LLM on this data
After you've added data, you can now train a model. Once the training is complete, you can view the eval results.

Training on free-tier is done here on Lamini servers (but if you're on enterprise tier, this can be done on your servers) and you can track the training job's progress at [this training interface](https://app.lamini.ai/train). Once it's done, you can view evaluation results and play with it on a playground, on the same page.

```python
results = model.train()
```

Once a model is trained you can check the eval results to see before and after comparisons of the base model and the trained model. 

```python
evaluation = model.evaluate()
print(evaluation)
```

You can also query the new trained model like so:

</details>
  <summary>Instantiate an<code>html form</code> to use as (test) input.</summary>

```python
html = Input(html_dom="""<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form>
        <div>
            <label for="first_name">First Name:</label><br>
            <input type="text" id="first_name" name="first_name" value="John" readonly>
        </div>
        <div>
            <label for="last_name">Last Name:</label><br>
            <input type="text" id="last_name" name="last_name" value="Doe" readonly>
        </div>
        <div>
            <label for="cc_number">Credit Card Number:</label><br>
            <input type="password" id="cc_number" name="cc_number" value="**** **** **** 1234" readonly>
        </div>
        <div>
            <input type="submit" value="Submit">
        </div>
    </form>
"""
```
</details>

Now run the `html` form into the finetuned model.
```python
extracted = model(html)
print(extracted)
```

See the extracted output!

_Output:_

````python
Output(first_name='John', last_name='Doe', credit_card_number='**** **** **** 1234')
````