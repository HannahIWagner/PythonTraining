print("1.Find the length of A given B and C \n2.Find the length of B given A and C \n3.Find the length of C given A and B")

option = int(input("Choose an option: "))

if option == 1:
    sideB = int(input("Please enter the length of side B: "))
    sideC = int(input("Please enter the length of side C: "))
    sideA = (sideB ** 2) + (sideC**2)
    print ("A=",sideA)
elif option == 2:
    sideA = int(input("Please enter the length of side A: "))
    sideC = int(input("Please enter the length of side C: "))
    sideB = (sideA ** 2) + (sideC**2)
    print ("B=",sideB)
elif option == 3:
    sideA = int(input("Please enter the length of side A: "))
    sideB = int(input("Please enter the length of side B: "))
    sideC = (sideA ** 2) + (sideB**2)
    print ("C=",sideC)
else:
    print("Not a valid input, try again")