quantity = int(input("Enter the number of disks, and the program will return " 
	"the number of moves needed to solve the problem (move all disks from"
	" tower A to tower C).\n"))
#Preparation: let's imagine three pegs, and make for each one a 
#corresponding vector. The leftmost peg has the specified number of disks on
#it, numbered from the smallest, topmost to the largest, bottom-most one.
A=[]
for i in range(quantity):
	A.append(i+1)
B=[]
C=[]
#Now, let"s start solving the problem. 



def MoveDisk(disk, source, dest):
	"""
	Moves a disk from the source peg to the destination peg.
	This is the only legal move in this game (provided that we do not put
	a bigger disk on top of a small one).

	The move counter should be declared globally, as it is called on by two
	functions and the program's body.
	"""
	global moves
	moves += 1
	source.remove(disk)
	dest.insert(0, disk)

def MoveTower(disk, source, dest, spare):
	"""
	Moves a tower of disks from the source peg to the destination peg,
	using the spare peg in the process.

	If the tower starts with disk 1 (the smallest one), it only contains that
	one. So we invoke our moving disk function straight away, and we're done.

	If the tower is bigger, we invoke this same function again (recursively),
	but on a tower without the largest disk. Eventually, we get to the case
	where our tower is again just the first (topmost) disk, and move it to the
	spare peg. After exiting that cycle, we execute the second command: move
	the second disk to the destination peg, and then move the first disk on
	top of it. If the number of disks was 2, we are done. Otherwise, we follow
	the same pattern.
	"""
	if disk == 1:
		MoveDisk(disk, source, dest)
		PrintLayout(A, B, C)
	else:
		MoveTower(disk-1, source, spare, dest)
		MoveDisk(disk, source, dest)
		PrintLayout(A, B, C)
		MoveTower(disk-1, spare, dest, source)

def PrintLayout(peg1, peg2, peg3):
	"""
	Outputs the current state of the three pegs.
	"""
	global moves
	print("Step " + str(moves) + ".\n        A: " + str(peg1) +
		"\n        " + "B: " + str(peg2) + "\n        " + "C: " + str(peg3))


#We must set the move counter to zero.
moves=0
#Now, we start the actual solving process:
MoveTower(quantity, A, C, B)
#Then we print the conclusion. The number of moves required is always the 
#Mersenne number corresponding to the number of disks.
print("\nThe number of moves required is " + str(moves))
