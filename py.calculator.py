print("Press 1 for addition \n Press 2 for subtraction \n press 3 for division \n press 4 for multiplication \n press 5 for exponential")

m=int(input("enter your choice"))
if m==1:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a+b
    print(c)
elif m==2:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a-b
    print(c)

elif m==2:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a
    print(c)
elif m==3:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a/b
    print(c)
elif m==4:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a*b
    print(c)

elif m==5:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a**b
    print(c)
else:
    print("enter specifed value only")
