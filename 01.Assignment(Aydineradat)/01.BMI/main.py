print("Challenge your BMI index")

h = float(input("Plz enter your height in meters"))
w = float(input("Plz enter your weight in kg"))

bmi = w / h **2

if bmi < 18.5:
     print("BMI: ", bmi ," you are very low weighted")
elif 18.5 <= bmi < 25:
     print("BMI: ", bmi ," you are in normal shape")
elif 25 <= bmi < 30:
     print("BMI: ", bmi ," you are overweighet")
elif 30 <= bmi < 35:
     print("BMI: ", bmi ," you are  obese")
elif 35 <= bmi < 40:
     print("BMI: ", bmi ," oh you are extremely obese") 