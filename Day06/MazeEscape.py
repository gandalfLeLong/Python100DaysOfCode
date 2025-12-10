#Small program solving a maze following only the wall on the right of the robot. This is suppose to be done in the reeborg.ca website, this code will only loop on infinity
#because of the absence of map or real movement functions

def move():
	print("Move forward")

def turnLeft():
	print("Turn left")

def turnRight():
	print("Turn right")

def frontIsClear():
	print("Front is clear")

def rightIsClear():
	print("Right is clear")

def	atGoal():
	print("At goal")

#Edge case where there is no wall on the right for 4 consecutive moves
while frontIsClear():
	move()
turnLeft()

while not atGoal():
	if rightIsClear():
		turnRight();
		move()
	elif frontIsClear:
		move()
	else:
		turnLeft()
