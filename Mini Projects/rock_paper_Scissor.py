import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def cals(value):
  for your in range (0,len(value)):
    if value[your] == 0 and your == 0:
      print("You chosen Rock"+rock)
    elif value[your] == 0 and your == 1:
      print("Computer chosen Rock"+rock)
    elif value[your] == 1 and your == 0:
      print("You Chosen Paper"+paper)
    elif value[your] == 1 and your == 1:
      print("Computer chosen Paper"+paper)
    elif value[your] == 2 and your == 0:
      print("You Chosen Scissors"+scissors)
    elif value[your] == 2 and your == 1:
      print("Computer chosen Scissors"+scissors)
    else:
      print(f"The Entered Number {your} is invalid")

def result(value):
  if value[0]==value[1]:
    print("The Match is Draw")
  elif value[0]==0 and value[1]==1 or value[0]==1 and value[1]==2 or value[0]==2 and value[1]==0:
    print("The computer wins the game and you lose")
    print("\n\n\n\n\nDon't Lose Your Hope")
  elif value[0]==1 and value[1]==0 or value[0]==2 and value[1]==1 or value[0]==0 and value[1]==2:
    print("You wins the Game and the computer lose")
    print("\n\n\n\n\nKeep on Going")

print(f"ROCK: {rock}\n PAPER: {paper}\n SCISSORS: {scissors}")
yours = input("What do you choose ?\nPress 0 for Rock,1 for Paper or 2 for Scissors\n")
comp_choice = random.randint(0,2)
value =[int(yours),comp_choice]
cals(value)
result(value)