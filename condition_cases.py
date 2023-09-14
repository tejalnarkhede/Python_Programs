while(True):
    print("------------------ Menu -----------------------")
    print("1.Area of circle\n2.Area of Triangle\n3.Area of Rectangle\n4.Factorial\n5.Prime")
    print("-----------------------------------------------")
    ch=int(input("Enter Your choice:"))
    if(ch==1):
        r=float(input("\nEnter the Radius:"))
        Area=3.14*r*r
        print("\n\tArea of Circle is:",Area)
    elif(ch==2):
        base=float(input("\nEnter the base:"))
        height=float(input("Enter the Height:"))
        Area=0.5*base*height
        print("\n\tArea of Triangle is:",Area)
    elif(ch==3):
        l=float(input("\nEnter the Length:"))
        b=float(input("Enter the Height:"))
        Area=l*b
        print("\n\tArea of Rectangle is:",Area)
    else:
        fact=1
        n=int(input("\nEnter the Number For finding its factorial:"))
        while(n>0):
            fact=fact*n
            n=n-1
        print("\n\tFactorial is:",fact)
    ch=int(input("\n\nDo u want to continue press 1:"))
    if(ch!=1):
        print("\n\tThank You!!!")
        break




