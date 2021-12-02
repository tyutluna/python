# a simple example for if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    # we can ignore case by lower the item before comparison
    if car.lower()=='bmw':
        print(car.upper())
    else:
        print(car.title())
