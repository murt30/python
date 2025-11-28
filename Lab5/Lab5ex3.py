import math

income = float(input("Enter monthly income: "))
pension = float(input("Enter pension payments: "))
cutoff = float(input("Enter cutoff point: "))

taxcredits = float(input("Enter tax credits: "))

if income > cutoff:

    
    paye=((cutoff*.2) + (.42*(income-cutoff-pension))-taxcredits)
    print("The PAYE due by this employee is %.2f"%paye,"EUR")
else:
    paye=(.2*(income-pension))-taxcredits
    print("The PAYE due by this employee is %.2f"%paye,"EUR")


