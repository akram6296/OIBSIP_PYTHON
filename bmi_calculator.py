print("WELCOME TO BMI CALCULATOR!")
print("**************************")
height=float(input('Enter your height in meter: '))
weight=float(input('Enter your weight in kg: '))
if 0.2<=height<2.5 and 1<=weight<500:
    bmi=weight/(height**2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi>0:
        if bmi <18.5:
            print("You are underweight")
        elif 18.5<=bmi<24.9:
            print("Your weight is normal")
        elif 24.9<=bmi<29.9:
            print("You are overweight")
        else:
         print("You have obesity")
    else:   
        print("Enter valid data!")
else:
    print("Please Enter Valid Data!")
