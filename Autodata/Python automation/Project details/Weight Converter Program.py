Weight = float(input("Please enter the Weight: "))
unit = input("Enter unit in LBS(l) or KGs (k): ")
if unit.upper()=='L':
    convert = Weight*0.45
    print(f"you are {convert} kilos")
else:
    convert = Weight/0.45
    print(f"You are {convert} pounds")