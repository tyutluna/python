# looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# name of the variable doesn't matter, but have to be matched.
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)