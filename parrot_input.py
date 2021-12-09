# input() function pauses your program and waits for the user to enter some text.
message = input("Tell me something, and I will repeat" + 
                "it back to you: ") 
print(message)

print("It can also make personal greetings.")
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# we can also store the prompt in a variable and pass that variable to the input
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("Hello, " + name + "!")

# when you need numerical input, you can use int() function to convert string
#  to int.
age = input("How old are you? ")
age = int(age)


