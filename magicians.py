magicians = ['alice', 'david', 'carolina']
# store elements in magician and print them
for magician in magicians:
    print(magician)

# the name of element doesn't matter, it's a temporary variable
# format  matters
for cat in magicians:
    print(cat)

# doing more work within a for loop
for magician in magicians:
    print(magician)
    print(magician.title() + ", that was a great trick!")
