#Calculate BMI

a = int(input("Enter your height (cm)? "))
b = int(input("Enter your weight (kg)? "))
c = a/100

BMI = b / (a*a)

if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI < 18.5:
    print("Underweight")
else:
    if 18.5 <= BMI < 25:
        print("Normal")
    elif 25 <= BMI < 30:
        print("Overweight")
    else:
        print("Obese")


