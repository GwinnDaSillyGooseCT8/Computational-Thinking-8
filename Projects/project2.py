Sat_points = 0
Jup_points = 0
Ear_points = 0
Mar_points = 0
Nep_points = 0
Ven_points = 0

print ("Hello! Welcome to the Alien Convention!!")
print ("What is your name?")
name = input()
if name == "67" or if name == "brainrot":
    print (" Your going to jail")
    input()
    input()
    input()
print (f" Nice to meet you {name}. You are taking this test to find out which type of planet your from!")
print ("There are jupiter, Saturn, Earth, Mars, Venus, and Neptune.")
print (" Please answer honestly and with the first letter capital! Thank you!")
input ("PRESS ENTER TO START")
answer1 = input (" Is your planet... A cold, B hot, C both ")
if answer1 == "A":
    Jup_points += 1
    Nep_points += 1
    Sat_points += 1
elif answer1 == "B":
    Ven_points += 3
elif answer1 == "C":
    Mar_points += 1
    Ear_points += 1

answer2 = input (" Is your planet a gas giant? ")
if answer2 == "Yes":
    Jup_points += 2
    Nep_points += 2
    Sat_points += 2
    Mar_points -= 3
    Ear_points -= 3
    Ven_points -= 3
elif answer2 == "No":
    Mar_points += 2
    Ven_points += 2
    Ear_points += 2
    Jup_points -= 3
    Nep_points -= 3
    Sat_points -= 3
print ("Alrighty..... prosesing")
answer3 = input (" How much differnt life is on your planet? A lot, B only us, C Little bit ")
if answer3 == "A":
    Ear_points += 5
elif answer3 == "B":
    Nep_points += 1
    Jup_points += 1
    Ven_points += 1
    Ear_points -= 3
elif answer3 == "C":
    Sat_points += 1
    Mar_points += 1
    Ear_points -= 3
answer4 = input (" Do you like it there? ")
if answer4 == "Yes":
    print ("Thats good!")
elif answer4 == "No":
    print ("Awwww why?")
print("Thank you so much for taking this quiz!! Here are your scores,")
print(f"You have {Mar_points} Mars, {Jup_points} Jupiter, {Ear_points} Earth, {Sat_points} Saturn, ")
print(f"{Nep_points} neptune, andd... {Ven_points} Venus!")
if Nep_points > Mar_points and Nep_points > Jup_points and Nep_points > Sat_points and Nep_points > Ven_points and Nep_points > Ear_points:
    print ("You are a Neptune alien! Have fun!")
elif Sat_points > Mar_points and Sat_points > Jup_points and Sat_points > Nep_points and Sat_points > Ven_points and Sat_points > Ear_points:
    print ("You are a Saturn alien! Have fun!")
elif Ear_points > Mar_points and Ear_points > Jup_points and Ear_points > Sat_points and Ear_points > Ven_points and Ear_points > Nep_points:
    print ("You are a Earth alien! Have fun!")
elif Jup_points > Mar_points and Jup_points > Ear_points and Jup_points > Sat_points and Jup_points > Ven_points and Jup_points > Nep_points:
    print ("You are a Jupiter alien! Have fun!")
elif Ven_points > Mar_points and Ven_points > Ear_points and Ven_points > Sat_points and Ven_points > Jup_points and Ven_points > Nep_points:
    print ("You are a Venus alien! Have fun!")
elif Mar_points > Jup_points and Mar_points > Ear_points and Mar_points > Sat_points and Mar_points > Ven_points and Mar_points > Nep_points:
    print ("You are a Mars alien! Have fun!")
else:
    print ("I can't detect where you are from, but still have fun!")
print(" Welcome to the convention!!")