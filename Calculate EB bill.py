unit = int(input("Enter the number of units : "))

if unit <= 100:
    amount = 0
    charge = 0
elif 100 < unit <= 200:
    amount =  unit*5.25
    charge = 50
elif 200 < unit <= 400:
    amount =  unit*7.75
    charge=70
elif 400 < unit <= 500:
    amount =  unit*9.25
    charge=80
else:
    print("Invalid Unit!!")

billTotal = amount + charge
print("Electricity unit : ", billTotal)
