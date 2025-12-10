import random

stop_flag = 0
rock_paper_scissors_list = ["Rock", "Paper", "Scissors"]
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice > 2:
	print("Wrong input, you lose.")
	stop_flag = 1
else:
	print(f"You chose {rock_paper_scissors_list[user_choice]}")

if stop_flag == 0:
	print(f"Computer chose {rock_paper_scissors_list[computer_choice]}")

	if computer_choice == user_choice:
		print("It's a draw.")
	elif (computer_choice == 0 and user_choice == 2):
		print("You lose !")
	elif (user_choice == 0 and computer_choice == 2):
		print("You win")
	elif (user_choice == computer_choice + 1):
		print("You win")
	else:
		print("You lose !")