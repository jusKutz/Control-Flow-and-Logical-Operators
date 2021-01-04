# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

L4 = year % 4
L100 = year % 100
L400 = year % 400

if L4 != 0:
  print("It is not a Leap year.")
elif L100 != 0:
  print ("It is a Leap year.")
elif L400 != 0:
  print ("It is not a Leap year")
else:
  print ("It is a Leap year.")