#Jacob Pawlak
#CS463G
#November 28th 2017
#Markov decision process


###################### IMPORTS ######################

import copy
from random import *

###################### PART 1 ######################

#Use value iteration to find the optimal policy with no discount and horizon 6 (in other words, find V^6 for all states).

def part1():

	#the reward table
	state_reward_func = [ [0,0,3,10],
				[0,5,0,60],
				[5,10,5,0],
				[45,0,0,5] ]

	#make a copy of the reward function for the utilities and directions,
	# the types in each won't matter by the end, thanks Python
	utility_func = copy.deepcopy(state_reward_func)
	directions = copy.deepcopy(state_reward_func)

	#out given probability
	prob_suc = .7
	prob_opp = .2
	prob_sta = .1

	#most of the commented print statements are there for debugging and I
	# dont want to delete them 
	#print()
	#print(utility_func)
	#print()

	#go for 6 horizons
	for horizon in range(1,7):

		#print("horizon:", horizon)
		#this copy will act as our U`, it will be the one we update systematically
		utility_copy = copy.deepcopy(utility_func)

		#loop over rows and cols
		for row in range(0,4):

			for col in range(0,4):

				#print("index:", (4 * row) + col + 1)

				#init the udlr vals
				up = 0
				down = 0
				left = 0
				right = 0

				#check for bound errors for UP
				if( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
					up = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )
				#bounds on bottom
				elif( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
					up = ( state_reward_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]) )
				else:
					up = ( state_reward_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
						(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )

				#check for bound errors for DOWN
				if( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
					down = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]) )
				#and bounds on top
				elif( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
					down = ( state_reward_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					down = ( state_reward_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
						(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]))

				#check for bound errors for LEFT
				if( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
					left = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))
				#and then again on the right
				elif( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
					left = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					left = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
						(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))

				#check for bound errors for RIGHT
				if( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
					right = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))
				#last time on the left
				elif( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
					right = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					right = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
						(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))

				#a cool lit dictionary that has our directional arrows in it
				# paired with the respective utility values
				vals = {"^": up, "v": down, "<": left, ">": right}
				#print(vals)
				#find the max value of those 4 utilities
				winner = max(vals.values())
				#print("max utility found was:", winner)
				#assign it to the copy for updating later
				utility_copy[row][col] = winner
				#small list of winners, notice we're not in there ;)
				winners = []
				#find the directions that have the winning utility
				for k,v in vals.items():
					if(v == winner):
						winners.append(k)
				#print(winners)
				#add that direction to the direction table
				directions[row][col] = winners
			#print()

		#here we assign a copy of the utils_copy back to the main util_func
		utility_func = copy.deepcopy(utility_copy)
		#print(utility_func)
		#print(directions)


	#pretty print the output for the user
	print()
	print("The final V^6:")
	for i in range(0,4):
		for j in range(0,4):
			print( round(utility_func[i][j], 3), end="  ")
		print()

	print()

	print("the final directions are:")
	for i in range(0,4):
		for j in range(0,4):
			print( choice(directions[i][j]), end="  ")
		print()

	print()

#call part1
part1()


###################### PART 2 ######################

#Use value iteration to find an optimal infinite-horizon, discounted policy with discount (gamma) = 0.96

def part2():

	#I will be leaving less comments here because 1) it's late, 2) most of this is the same as part1, and
	# the differences i will comment on

	state_reward_func = [ [0,0,3,10],
				[0,5,0,60],
				[5,10,5,0],
				[45,0,0,5] ]

	utility_func = copy.deepcopy(state_reward_func)
	directions = copy.deepcopy(state_reward_func)

	prob_suc = .7
	prob_opp = .2
	prob_sta = .1
	#need this discount value and the error value epsilon
	discount = .96
	epsilon = .001

	utility_copy = copy.deepcopy(utility_func)

	#instead of looping for 6 horizons, we are going to loop until we 
	# converge and our delta becomes super small
	while( True ):
	
		#setting delta here, init at 0 because we have not seen any
		# differences yet
		delta = 0

		for row in range(0,4):

			for col in range(0,4):

				#print("index:", (4 * row) + col + 1)
				#print("delta:", delta)

				#init the udlr vals
				up = 0
				down = 0
				left = 0
				right = 0

				if( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
					up = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )
				elif( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
					up = ( state_reward_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]) )
				else:
					up = ( state_reward_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
						(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )

				if( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
					down = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]) )
				elif( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
					down = ( state_reward_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					down = ( state_reward_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
						(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]))

				if( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
					left = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))
				elif( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
					left = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					left = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
						(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))

				if( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
					right = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))
				elif( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
					right = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					right = ( state_reward_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
						(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))

				vals = {"^": up, "v": down, "<": left, ">": right}
				#print(vals)
				winner = max(vals.values())
				#print("max utility found was:", winner)
				#now here we want to multiply our winner by the discount so that we can see it converge
				utility_copy[row][col] = winner * discount
				winners = []
				for k,v in vals.items():
					if(v == winner):
						winners.append(k)
				#print(winners)
				directions[row][col] = winners

				#re eval delta
				delta = max(delta, abs(utility_copy[row][col] - utility_func[row][col]))

		#you know the drill here.
		utility_func = copy.deepcopy(utility_copy)
		
		#this is our sentinel value, if the max difference is less than our max diff error, we can stop
		if(delta < (epsilon * (1 - discount) / discount)):	
			
			#pretty print once more
			print("The final V*:")
			for i in range(0,4):
				for j in range(0,4):
					print( round(1.04165 * utility_func[i][j], 3), end="  ")
				print()

			print()

			print("the final directions are:")
			for i in range(0,4):
				for j in range(0,4):
					print( choice(directions[i][j]), end="  ")
				print()

			print()
			
			return

		#print(utility_func)
		#print(directions)

#call part2
part2()
