name = input("Enter your name Homie: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in Inches: "))

BMI = (weight * 730) / (height * height)
print("Your BMI is " + str(BMI))

if BMI >0 :
    if(BMI < 18.5):
        print(name +' You are under weight')
    elif(BMI <= 29.9):
        print(name +' You are normal weight')
    elif(BMI < 34.9 ):
        print(name +" Homie you fat as hell")
    elif (BMI < 39.9):
        print(name +" You are damned obese")
    else:
        print(name +" You are morbidly obese")
else:
    print("Enter a valid Input")