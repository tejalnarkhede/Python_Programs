def add():
    print(' i am in add function')
    global a,b
    a=10
    b=2
    c=5
    print("Multiplication is:",a*b)

add()

def func():
    print('i am in func function')
    print(a)
    print(b)
    print(c)
func()