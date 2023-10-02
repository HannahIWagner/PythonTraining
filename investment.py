initial = 100
target = 1000
interest_rate = 1.1
current = initial
numyears = 0

while current < target:
    current = current * interest_rate
    numyears += 1
print(f"It took you {numyears} years to reach £{target} starting from £{initial}")