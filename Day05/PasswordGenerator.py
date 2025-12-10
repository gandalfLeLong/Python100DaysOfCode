#small program creating a password base on the numbers of letters, symbols and numbers an user want

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nb_letters= int(input("How many letters would you like in your password?\n")) 
nb_symbols = int(input("How many symbols would you like?\n"))
nb_numbers = int(input("How many numbers would you like?\n"))
buffer = ""
password = ""

for i in range(0, nb_letters):
	buffer += random.choice(letters)
for i in range(0, nb_symbols):
	buffer += random.choice(symbols)
for i in range(0, nb_numbers):
	buffer += random.choice(numbers)

for i in range(0, len(buffer)):
	character = random.choice(buffer)
	password += character
	buffer = buffer.replace(character, "", 1)

print(password)
