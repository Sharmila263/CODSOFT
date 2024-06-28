import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '_', '-']

print("Welcome to Password Generator! \n")


length = int(input("Enter the desired password length: "))


if length < 6:
    print("Password length should be at least 6 characters. Setting length to 6.")
    length = 6


n_letters = random.randint(1, length - 2)
n_symbols = random.randint(1, length - n_letters - 1)
n_numbers = length - n_letters - n_symbols

password_list = []


for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))


if length >= 6:  
    random.shuffle(password_list)

password = ''.join(password_list)
print("Generated Password:", password)
