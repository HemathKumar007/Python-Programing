a=int(input("enter the mark out of 100:"))
if(a<=35):
    print("poor student")
elif (a>35 and a<70):
    print("avg student")
elif (a>=70 and a<=100):
    print("good student")
else:
    print("the number is invalid")
