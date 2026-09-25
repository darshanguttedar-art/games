operator=input("enter an operator (+,-,*,/) :")

num1=float(input("enter the first number:"))
num2=float(input("enter the 2nd number:"))



if operator=="+":
    print(f"num1 + num2={num1+num2}")

elif operator=="-":
    print(f"substration of num1 - num2 :{num1-num2}")

elif operator=="*":
    print(f"multiplication of the num1 * num2: {num1 * num2}")

elif operator=="/":
    print(f"division num1/num2:{num1/num2}")

else:
    print("invalid operator")
    