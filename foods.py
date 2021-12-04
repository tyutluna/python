# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Without [:], the two variables will always be the same

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
