# convert user's input from string to integer.
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")