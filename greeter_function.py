# def is the keyword to inform python that you're defining a function.
# here is a simple function named greet_user()
def greet_user():
    """"Display a simple greeting."""
    print("Hello!")

# call the function 
greet_user()

# a function with one parameter
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

# call the function with paramenter
greet_user('jesse')
