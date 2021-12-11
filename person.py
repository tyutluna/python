# function can return any kind of value
# return a dictionary
def build_person(first_name, last_name):
    """"Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# we can easily extend this function to accept optional values
def build_person(first_name, last_name, age = ''):
    """"Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']= age
    return person

musician = build_person('jimi', 'hendrix')
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)
