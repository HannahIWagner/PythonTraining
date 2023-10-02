min = 1
max = 100
attempts = 0

while attempts <3:
    num = int(input(f"Please enter a number between {min} and {max}: "))
    if num <=100 and num >=1:
        print (num)
        break
    attempts += 1
if attempts >=3:
    print("None")
