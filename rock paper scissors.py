print("enter 0 for rock 1 for paper and 2 for scissors")
a = int(input("what will you choose "))
import random
b = random.randint(0,2)
Rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper ='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, Paper, Scissors]
print(game_images[a])
print("computer choose" + game_images[b])

if(a == 0 and b == 2):
    print("You win")
elif(a == 2 and b == 1):
    print("you win")
elif(a==1 and b == 0):
    print("you win")
elif(a == b):
    print ("draw")
else:
    print("You loose")

