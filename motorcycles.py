motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change element
motorcycles[0]='ducati'
print(motorcycles)

# adding elements to a list
motorcycles.append('ducati')
print(motorcycles)

# inserting elements into a list, as the first element
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove an element and no longer access the value that was removed
del motorcycles[0]
print(motorcycles)

# remove an element and can access the value that was removed
# pop() removes the last item in a list
motorcycles=['honda', 'yamaha', 'suzuki']
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# remove an element by value
motorcycles=['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)