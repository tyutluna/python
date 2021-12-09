# we can nest a dictionary inside another dictionary.
# there are two users with their informationa dictionaries in a dictionary.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    # get the information in each dictionary
    print("\nUsername: " + username)
    full_name= user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    # print out the information stored
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

