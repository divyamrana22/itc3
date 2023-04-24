a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))

if a+b>c:
    if b+c>a:
        if c+a>b:
            print("YES!!!")
else:
    print("NO!!!!")
