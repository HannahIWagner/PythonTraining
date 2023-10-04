companies = []
sales = []

with open("carSale.csv") as file1:
    lines = file1.readlines()

for x in range(len(lines)):
    if x % 2 ==0:
        companies.append(lines[x])
    else:
        data = lines[x].strip().split(',')
        sales.append (list(map(int, data)))

totalByMonth = [0,0,0,0,0]

for i in range(len(sales)):
    for j in range(len(totalByMonth)):
        totalByMonth[j] += sales[i][j]
    
print(totalByMonth)

for i in sales:
    print(sum(i))

#print(companies)
#print(sales)