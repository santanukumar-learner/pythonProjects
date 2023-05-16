import random
from game_data import data
from art_HL import logo, vs
print(logo)
score = 0
b = random.choice(data)

def format_game(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description},{account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

game_should_continue = True
while game_should_continue:
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)


    print(f"compare a: {format_game(a)}")
    print(vs)
    print(f"against b: {format_game(b)}")
    guess = input("Who has more follower type 'a' or 'b'").lower()
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]
    c = check_answer(guess, a_followers, b_followers)
    points = 0
    if c:
        score += 1
        print(f"You are right. score: {score}")

    else:
        game_should_continue = False
        print(f"Sorry you are wrong. score: {score}")


