operator=input("enter an operator (+,-,*,/) :")

num1=float(input("enter the first number:"))
num2=float(input("enter the 2nd number:"))



if operator=="+":
    result = num1 + num2
    print(f"num1 + num2=round({result}, 2)")

elif operator=="-":
    result = num1 - num2
    print(f"substration of num1 - num2 :{round(result, 2)}")

elif operator=="*":
    result = num1 * num2
    print(f"multiplication of the num1 * num2:{round(result, 2)}")

elif operator=="/":
    result = num1 / num2
    print(f"division num1/num2: {round(result, 2)}")

else:
    print("invalid operator")
    