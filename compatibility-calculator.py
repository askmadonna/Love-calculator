print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

T1 = lower_name1.count("t")
R1 = lower_name1.count("r")
U1 = lower_name1.count("u")
E1 = lower_name1.count("e")
T2 = lower_name2.count("t")
R2 = lower_name2.count("r")
U2 = lower_name2.count("u")
E2 = lower_name2.count("e")
L1 = lower_name1.count("l")
O1 = lower_name1.count("o")
V1 = lower_name1.count("v")
E3 = lower_name1.count("e")
L2 = lower_name2.count("l")
O2 = lower_name2.count("o")
V2 = lower_name2.count("v")
E4 = lower_name2.count("e")
score3 = (T1 + T2 + R1 + R2 + U1 + U2 + E1 + E2 )
score4 = (L1 + L2 + O1 + O2 + V1 +V2 + E3 + E4 )
score1 = str(score3)
score2 = str(score4)
score5 = (score1 + score2)
score = int(score5)
if score>90 or score<10:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


