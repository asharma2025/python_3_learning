# Your code below:
# Creating lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Count occurance of 2 in prices
num_two_dollar_slices = prices.count(2)

# Length of toppings
num_pizzas = len(toppings)

# 2 dimensional list for pizza and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Sort pizza and prices in ascending order
pizza_and_prices.sort()

# Find cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# Find priciest pizza
priciest_pizza = pizza_and_prices[-1]

# Remove anchovies from list
pizza_and_prices.pop()

# Add peppers pizza to list
pizza_and_prices.insert(4, [2.5, "peppers"])

# Find 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]

# print statements
print(num_two_dollar_slices)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

print(pizza_and_prices)

print(three_cheapest)