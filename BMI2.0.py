# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

H = float(height)
W = float(weight)

BMI = (round(W / (H**2)))

if BMI < 18.5:
  print ("you are under weight.")
elif BMI <=25 :
  print ("you have a normal weight.")
elif BMI <=30:
  print ("you are overweight.")
elif BMI <=35:
  print ("you are obese.")
else:
  print ("you are clinically obese.")