def getIncomeTax(salary):
    if  0 <= salary <= 34500:
        salary *= 0.2
    elif salary >=34501 and salary <=150000:
        salary *= 0.4
    else:
        salary *= 0.45
    return salary

if __name__== "__main__":
    initial_salary = 11850
    tax_amount = getIncomeTax(initial_salary)
    print(tax_amount)
