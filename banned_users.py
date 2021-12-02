# check whether a value is in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user.lower() in banned_users:
    print(user.title() + ", you are banned.")
    # we can also check whether a value is not in a list
elif user.lower() not in banned_users:
    print(user.title() + ", you can post a response if you wish.")