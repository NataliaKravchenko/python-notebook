#4
import os.path
if os.path.isfile('housing.data.py'):
    print ("I have a file to process")
else:
    print ("Boo, no file for me")

#5
f = open('housing.data.py', 'r')
print(f.read())

#6
for line in f:
    print(line, end='')

#7
print(list(f))