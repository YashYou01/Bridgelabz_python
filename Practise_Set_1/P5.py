salary=50000
newsalary=salary
late=int(input("Enter number of late days: "))
absent=int(input("Enter number of absent days: "))

if late>10 :
    newsalary=salary-(10/100)*salary
elif late>5 :
    newsalary=salary-(5/100)*salary

again=newsalary

if absent>2:
    again=newsalary-(5/100)*salary

print(again)


