# you can work with a specific group of items in a list, which python calls a slice.

# print a slice of the list, which are the first three values.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# we can also write as belowe, which starts at the beginning
print(players[:3])

# print second, third and fourth items
print(players[1:4])

# print all items from the thrid item through the last item
print(players[2:])

# print the last three items
print(players[-3:])

# loop through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    