salary=int(input("enter the salary amount:"))
age=int(input("enter the age:"))
if(salary>=200000 or age<=25):
    loan=int(input("enter the loan amount:"))
    if(loan>50000):
        print("loan should be max")
    else:
         print("loan shouild be requird")
    print("eligible for loan")
else:
    print("not eligible for loan")
