a = 50
b = a
print(id(a))
print(id(b))
# Reassigned variable a
a = 500
print(id(a))
print("-------------------------------")
print('\nAssining same value to multiple varibles')
x=y=z=36
print(id(x))
print(id(y))
print(id(z))
print('--------------------------------')
print('\nAssining different values to multiple varibles')
x,y,z=5,6,7
print("x=",x)
print("y=",y)
print("z=",z)
print("\n")
print(id(x))
print(id(y))
print(id(z))
