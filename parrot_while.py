prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
# an example for while-loop, which will print the end signal as well.
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# add an if statement to avoid printing the end message.
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# we can also achive it by adding a flag.
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False # or we can use break to exit the while loop
                       # immediately without running any remaining code in the loop.
    else:
        print(message)
