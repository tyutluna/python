# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print ("\nFinished making your pizza!")

# we cannot use if-elif-else here, because it will stop when one condition is met.

# we can also write it by a for loop
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

# in the loop, we can use if statement
for requested_topping in requested_toppings:
    if requested_topping=='green pepper':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

# before the for loop, we can check whether  the list is empty
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# we can compare multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', ' extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
