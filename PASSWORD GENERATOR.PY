import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator")
number_of_letters = int(input("Enter number of letter you want in your password"))
number_of_numbers = int(input("Enter number of number you want in your password"))
number_of_symbols = int(input("Enter number of symbols you want in your password"))
#[] is symbol for list while "" is symbol for string
password = []
for char in range(1, number_of_letters+1):
    password.append(random.choice(letters))
for char in range(1, number_of_numbers+1):
    password.append(random.choice(numbers))
for char in range(1, number_of_symbols+1):
    password.append(random.choice(symbols))
random.shuffle(password)
print(password)
new_password = ""
for char in password:
    new_password += char
#you can't add string to list
print(new_password)


#hard
