import random
user = int(input("WHAT DO YOU CHOOSE? \nTYPE 0 FOR ROCK 1 FOR PAPER 2 FOR SCISSORS : "))
if user == 0:
    print("YOU CHOSE ROCK")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif user == 1:
    print("YOU CHOSE PAPER")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif user == 2:
    print("YOU CHOSE SCISSORS")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("INVALID INPUT")

comp = random.randint(0,2)
if comp == 0:
    print("COMPUTER CHOSE ROCK")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif comp == 1:
    print("COMPUTER CHOSE PAPER")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif comp == 2:
    print("COMPUTER CHOSE SCISSORS")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if user == comp:
    print("OOPS, IT'S A DRAW")
elif user == 0 and comp == 1:
    print("SO SORRY, YOU LOST!")
elif user == 1 and comp == 2:
    print("SO SORRY, YOU LOST!")
elif user == 2 and comp == 0:
    print("SO SORRY, YOU LOST!")
else:
    print("YAYYYYY! YOU WON")
