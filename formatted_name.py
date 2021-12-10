# a function with a simple return value
def get_formatted_name(first_name, last_name):
    """"Return a full name, nearly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# we can improve this function by adding an default value for middle name.
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# call the function in two ways
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)