# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name= name1 + name2
lower_case_name = combined_name.lower()


T = lower_case_name.count('t')
R = lower_case_name.count('r') 
U = lower_case_name.count('u') 
E = lower_case_name.count('e') 

true = T + R + U + E

L = lower_case_name.count('l') 
O = lower_case_name.count('o') 
V = lower_case_name.count('v') 
E = lower_case_name.count('e')

love = L + O + V + E


result = str(true) + str(love)
result_int = int(result)

if result_int < 10 or result_int > 90:
  print(f"Your score is {result_int}, you go together like coke and mentos.")

elif result_int > 40 and result_int < 50:
  print(f"Your score is {result_int}, you are alright together.")

else:
  print (f"Your score is {result_int}")