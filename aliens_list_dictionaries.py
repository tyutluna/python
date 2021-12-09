alien_0 ={'color': 'green', 'point': 5}
alien_1 ={'color': 'yellow', 'point': 10}
alien_2 ={'color': 'yellow', 'point': 15}

aliens = [alien_0, alien_1,alien_2]

for alien in aliens:
    print(alien)

# make 30 green aliens.
#make an empty list for storing aliens.
aliens =[]
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow',}
    aliens.append(new_alien)

# we can change some of them.
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['point']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['point']=15

# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))