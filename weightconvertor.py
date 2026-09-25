weight=float(input("enter the weight:"))

unit=input("kilogram or pounds ? (k or l):")

if unit=="K":
    weight =weight*2.205
    unit="Lbs."
elif unit=="L":
    weight  =weight/2.205
    unit="kgs"

else:
    print("invalid unit")

print(f"the weight is :{round(weight, 2)} {unit}")
