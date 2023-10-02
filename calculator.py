Number1=int(input("Choose a number: "))
Number2=int(input("Choose another number: "))

Calculator= "1.Add + \n2.Subtract - \n3.Multiply * \n4.Divide / \n5.Square s"
print (Calculator)
operation = input("Please select which operation to perform (1-5): ")

if operation == "+":
    res = Number1 + Number2
    print (res)
elif operation == "-":
    res = Number1 - Number2
    print (res)
elif operation == "*":
    res = Number1 * Number2
    print (res)
elif operation == "/":
    res = Number1 / Number2
    print (res)
elif operation == "s":
    res = Number1 ** Number2
    print (res)
else:
    print("Not a valid operation, try again")