import random
from art import logo
print(logo)
c = random.randint(0, 100)
# make a function to choose difficulty


def difficulty():
    a = input("Enter 'h' for high difficulty and 'l' for lower difficulty: ").lower()
    if a == "h":
        lives = 5
    else:
        lives = 10
    return lives


life = difficulty()
game_over = False
while not game_over:
    b = int(input("Enter a number between 0 to 100"))
    if c == b:
        print("You win")
        game_over = True

    elif c < b:
        print("You have choose a bigger number.")
        life -= 1
        print(f"you have {life} life left.")
        if life == 0:
            game_over = True
            print("You loose")
    elif c > b:
        print("You have choose a smaller number.")
        life -= 1
        print(f"you have {life} life left.")
        if life == 0:
            game_over = True
            print("You loose")
