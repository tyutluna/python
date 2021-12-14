# The asterisk in the parameter name to make an empty tuple 
# and pack whatever values it receives into this tuple.

def make_pizza(*toppings):
    """"Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# If you want a function to accept several different kinds of arguments, 
# the parameter that accepts an arbitrary number of arguments must be placed 
# last in the function definition.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')