# a function with two paramenters
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# call the function with parameters, order matters.
describe_pet('hamster', 'harry')
# you can call a function as many times as needed.
describe_pet('dog', 'willie')

# keyword arguments free you from having to worry about correctly ordering 
# your arguments in the function call
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# we can use a default value as paramter, normally it's the second parameter
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# we can call the function as below
describe_pet(pet_name = 'willie')
# same with below
describe_pet('willie') # call like this, the paramenter 
                       # will be considered as the first one

# we can also change the default value when we call the function 
describe_pet(pet_name = 'harry', animal_type = 'hamster')