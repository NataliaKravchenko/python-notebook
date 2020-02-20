#4
import os.path
if os.path.isfile('housing.data.py'):
    print ("I have a file to process")
else:
    print ("Boo, no file for me")

#5
f = open('housing.data.py')
print(f.read())

for line in f:
    print(line, end='')

print('I love {} for "{}!"'.format('Geeks', 'Geeks'))



