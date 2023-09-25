print("Welcome to BMI Calculator!!!!")

Weight = input("Enter your Weight(kg) ")
Height = input("Enter your Height(m)    ")

bmi = float(Weight) / (float(Height) ** 2)

bmi = round(bmi, 1)
print(bmi)

if bmi <= 18.5:
    #print(f"Your BMI is {bmi}. You are Underweight.")
    print("Your BMI is {}. You are Underweight." .format(bmi))
   #print(f"Your BMI is" + bmi +. You are Underweight.".format(bmi))
elif 18.5 > bmi <= 25:
    print(f"Your BMI is {bmi}. You are Normal.")
elif 25 < bmi <= 30:
    print(f"Your BMI is {bmi}. You are Overweight.")
else:
    print(f" Output: You BMI is {bmi}. You are Obese. ")