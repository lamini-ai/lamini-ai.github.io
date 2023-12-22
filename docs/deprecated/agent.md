It is easy to build agents. 

We've provided an [open-source `Operator` repo](https://github.com/lamini-ai/llm-operator/) to built an agent (`Operator`) using open-source LLMs. 

You can also use your own framework to do this. Keep in mind that most agent frameworks are built specifically for a particular model or workflow.

For example, here is a food delivery agent:
```python
food_operator = FoodDeliveryOperator()

food_operator.add_operation(food_operator.search)
food_operator.add_operation(food_operator.order)

food_operator.train(<training_file>, <operator_save_path>)
response = food_operator("I want 10l of milk.")
```

Here is the Food Delivery Operator's thought process and plan:
```
Query: Add 2 gallons of milk to my cart.

selected operation: order
inferred arguments: {'item_name': 'milk', 'quantity': '2', 'unit': 'gallons'}

It is indicated that the user wants to invoke cart/order operation.
Calling orders API with: item_name=milk, quantity=2, unit=gallons
```

### Chat x Operator
LLM Operators can work hand in hand with your other LLMs, e.g. for Q&A, chat, etc.:
```
self.chat = LlamaV2Runner() # inside Operator class, pass in a model_name to a finetuned LLM if desired
...
message = user_input + orders_api_response
model_response = self.chat(message, system_prompt=f"Respond to the user, confirming the addition to cart. If response from API is 200, then confirm that the item {item_name} has been placed in the cart, else ask the user to restate their order.")
```


### Finetuning the Operator

We include ~30 super simple datapoints to get a boost in performance, beyond just prompt-engineering. A few rows of data:

| class_name | data                                               |
|------------|----------------------------------------------------|
| search     | "how do i track deliveries? substitutions?"       |
| order      | "I'd like to buy a bag of granny smith apples"    |
| noop       | "sometimes I dream of home"                        |


## Create your own Operator

Create an `Operator` class.

Create operations (functions) that you want the Operator to invoke. Here is the `order` operation for ordering food: 
```
def order(self, item_name: str, quantity: str, unit: str):
   """
   User wants to order items, i.e. buy an item and place it into the cart. This includes any indication of wanting to checkout, or add to or modify the cart. It includes mentioning specific items, or general turn of phrase like 'I want to buy something'.
   
   Parameters:
   item_name: name of the item that the user wants to order.
   quantity: quantity of the item that the user wants to order.
   unit: unit of the item that the user wants to order like kilograms, pounds, etc.
   """
```

You can prompt-engineer the docstring! The main docstring and parameter descriptions are all read by the LLM Operator to follow your instructions. This will help your Operator learn the difference between operations and what parameters it needs to extract for each operation.

Next, in the Operator's main call function, register each of your operations in your class init function, e.g.:
```
operator.add_operation(self.order)
operator.add_operation(self.search)
...
```

Finally, finetune your Operator!

```
training_data = "data/food_delivery.csv" # extra training data (optional)
operator_save_path = "models/FoodDeliveryOperator/" # dirpath to save operator for use later

operator.train(training_data, operator_save_path)
```

[Clone the repo](https://github.com/lamini-ai/llm-operator/).