# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()


T1 = name1_lower.count('t')
T2 = name2_lower.count('t')
T = T1 + T2

R1 = name1_lower.count('r') 
R2 = name2_lower.count('r') 
R = R1 + R2

U1 = name1_lower.count('u') 
U2 = name2_lower.count('u') 
U = U1 + U2

E1 = name1_lower.count('e') 
E2 = name2_lower.count('e') 
E = E1 + E2

true = T + R + U + E

L1 = name1_lower.count('l') 
L2 = name2_lower.count('l') 
L = L1 + L2

O1 = name1_lower.count('o') 
O2 = name2_lower.count('o') 
O = O1 + O2

V1 = name1_lower.count('v') 
V2 = name2_lower.count('v') 
V = V1 + V2

E1 = name1_lower.count('e')
E2 = name2_lower.count('e')
E = E1 + E2

love = L + O + V + E


result = str(true) + str(love)
result_int = int(result)

if result_int < 10 or result_int > 90:
  print(f"Your score is {result_int}, you go together like coke and mentos.")

elif result_int > 40 and result_int < 50:
  print(f"Your score is {result_int}, you are alright together.")

else:
  print (f"Your score is {result_int}")