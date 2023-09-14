tup=("Hi","Python",2)
print(type(tup))
print(tup)
print(tup[1:])
print(tup[0:2])
print(tup+tup)
print(tup*2)
#You can't modify value in tuples..it is read only data type..There is error in output...
tup[0]="Hello"

#output
#<class 'tuple'>
#('Hi', 'Python', 2)
#('Python', 2)
#('Hi', 'Python')
#('Hi', 'Python', 2, 'Hi', 'Python', 2)
#('Hi', 'Python', 2, 'Hi', 'Python', 2)
#    tup[0]="Hello"
#TypeError: 'tuple' object does not support item assignment
