grade= int(input("What is your grade? "))

if grade <1 or grade >100:
    print("Error: marks must be between 1 and 100")
elif grade <=50:
    print("Fail")
elif grade >=50 and grade <=60:
    print("Pass")
elif grade >=61 and grade <=70:
    print("Merit")
elif grade >=71 and grade <=100:
    print("Distinction")