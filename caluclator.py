# This program is a simple calculator to perform ALU for two inputs using function

while True:
    
    print()
    print("\t\t\t\t***Welcome to the calculator***")
    print()
    print("1.Addition\t\t2.Subtraction\t\t3.Multiplication\t\t4.Division")
    print()

    try:

        i = int(input("Choose your operation, enter from 1 to 4: "))
        print()

        def add(a,b):
            return a+b

        def sub(a,b):
            return a-b

        def mul(a,b):
            return a*b

        def div(a,b):
            return a/b
        
        if i==1:
            print("You chose Addition")
            print()
            a1=float(input("Enter first number: "))
            a2=float(input("Enter second number: "))
            print()
            print("The Sum is: ",add(a1,a2))

        elif i==2:
            print("You chose Subtraction")
            print()
            a1=float(input("Enter first number: "))
            a2=float(input("Enter second number: "))
            print()
            print("The Difference is: ",sub(a1,a2))

        elif i==3:
            print("You chose Multiplication")
            print()
            a1=float(input("Enter first number: "))
            a2=float(input("Enter second number: "))
            print()
            print("The Product is: ",a3 = mul(a1,a2))

        elif i==4:
            print("You chose Divison")
            print()
            a1=float(input("Enter first number: "))
            a2=float(input("Enter second number: "))
            print()
            print("The Division of", a1,"/",a2, "is: ", div(a1,a2))

        else:
            print("Invalid Input")

    except ValueError:
        print()
        print("Invalid Input. The program will now terminate.")
    print()

    re = input("Press 'y' if you want to calculate again: ")
    print()
    if re.upper() != 'Y':
        break
print()
