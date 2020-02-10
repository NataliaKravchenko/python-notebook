# Python Script 1
mynumber=1
myfloat=3.14
mystring='Hello World!'
myboolean=True
mylist=[1,2,3,4,5]

print(mynumber)
print(myfloat)
print(mystring)
print(myboolean)
print(mylist)

print(f'{type(mynumber)}, {type(myfloat)}, {type(mystring)}, {type(myboolean)}, {type(mylist)}')

#Python Script 2
my_list=[1,2,3,4,5,6,7,8,9]
selection=my_list[3:8]
new_list=selection*2
print(new_list)

#Python Script 3
print(my_list[0:][::2])
print(my_list[1:][::2])

#Python Script 4
x = list(range(1,101))
for i in x:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
