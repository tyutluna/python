# a simple dictionary store information of a alien
# a dictionary is a collection of key-value pairs. Each key is connected to a 
# value, you can use a key to access the value associated with that key.
# key1 : value1, key2 : value2 ...
alien_0 = {'color': 'green', 'point':5}
print("print the values in the alien dictionary\n")
print(alien_0['color'])
print(alien_0['point'])

new_points = alien_0['point']
print("You juest earned " + str(new_points) + " points!")

# add more key-value pairs of the dictionary, order does not matter
alien_0 ['x_position']=0
alien_0 ['y_position']=25
print(alien_0)
# we can also start with an empty dictionary and add information in it. 

# to modify a value in a dictionary
print("change the value of the alien dictionary\n")
print("The alien is " + alien_0['color'] + ".")
alien_0 ['color']='yellow'
print("The alien is now " + alien_0['color'] + ".")

print("add more information in the alien dictionary\n")
alien_0['speed']='medium'
print("original x-position: " + str(alien_0['x_position']))

# move the alien to the right
# determine how far to move the alien based on its current speed.
if alien_0['speed']=='slow':
    x_increment =1
elif alien_0['speed']== 'medium':
    x_increment=2
else:
    #this must be the fast alien
    x_increment=3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position']+ x_increment
print("New x-position: " + str(alien_0['x_position']))

# removing key-value pairs
print("remove some information of the dictionary\n")
print(alien_0)
del alien_0['point']
print(alien_0)
