# A small algorythm in python to cypher and decypher a message using an ofset
alive = True
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(original_text, offset):

	letter_index = 0
	encrypted_message = ""

	for letter in original_text:
		if letter in alphabet:
			letter_index = alphabet.index(letter) + offset
			letter_index %= len(alphabet)
			encrypted_message += alphabet[letter_index]
		else:
			encrypted_message += letter

	print(f"Your encrypted message is : {encrypted_message}")

def decrypt(original_text, offset):

	letter_index = 0
	decrypted_message = ""

	for letter in original_text:
		if letter in alphabet:
			letter_index = alphabet.index(letter) - offset
			letter_index %= len(alphabet)
			decrypted_message += alphabet[letter_index]
		else:
			decrypted_message += letter

	print(f"Your decrypted message is : {decrypted_message}")

def ceasar(original_text, offset, user_input):
	if user_input == "decode":
		decrypt(original_text, offset)
	elif user_input == "encode":
		encrypt(original_text, offset)
	else:
		print("Wrong user input")

while alive == True:
	user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
	text = input("Type your message :\n").lower()
	offset = int(input("Type de shift number :\n"))
	ceasar(text, offset, user_input)
	redo = input("Type 'yes' if you want to go again. Otherwise type 'no' :\n").lower()
	if redo != "yes":
		alive = False