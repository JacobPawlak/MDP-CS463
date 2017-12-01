#Jacob Pawlak
#CS463G
#November 28th 2017
#Markov decision process


###################### IMPORTS ######################

import copy

###################### PART 1 ######################

#Use value iteration to find the optimal policy with no discount and horizon 6 (in other words, find V^6 for all states).

def part1():

	state_reward_func = [ [0,0,3,10],
				[0,5,0,60],
				[5,10,5,0],
				[45,0,0,5] ]

	utility_func = copy.deepcopy(state_reward_func)
	directions = copy.deepcopy(state_reward_func)

	prob_suc = .7
	prob_opp = .2
	prob_sta = .1

	print()
	print(utility_func)
	print()

	for horizon in range(1,6):

		print("horizon:", horizon)
		utility_copy = copy.deepcopy(utility_func)

		for row in range(0,4):

			for col in range(0,4):

				print("index:", (4 * row) + col + 1)

				#init the udlr vals
				up = 0
				down = 0
				left = 0
				right = 0

				#check for bounds on top
				if( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
					up = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )
				#bounds on bottom
				elif( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
					up = ( utility_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]) )
				else:
					up = ( utility_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
						(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )

				#check for bounds on bottom
				if( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
					down = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]) )
				#and bounds on top
				elif( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
					down = ( utility_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					down = ( utility_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
						(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]))

				#check for bounds on left
				if( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
					left = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))
				#and then again on the right
				elif( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
					left = ( utility_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					left = ( utility_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
						(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))

				#check for bounds on right
				if( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
					right = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
						(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))
				#last time on the left
				elif( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
					right = ( utility_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
						(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
				else:
					right = ( utility_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
						(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))

				vals = {"up": up, "down": down, "left": left, "right": right}
				print(vals)
				winner = max(vals.values())
				print("max utility found was:", winner)
				utility_copy[row][col] = winner
				winners = []
				for k,v in vals.items():
					if(v == winner):
						winners.append(k)
				print(winners)
				directions[row][col] = winners
			print()

		utility_func = copy.deepcopy(utility_copy)
		print(utility_func)
		print(directions)

#part1()


###################### PART 2 ######################

#Use value iteration to find an optimal infinite-horizon, discounted policy with discount (gamma) = 0.96

def part2():

	state_reward_func = [ [0,0,3,10],
				[0,5,0,60],
				[5,10,5,0],
				[45,0,0,5] ]

	utility_func = copy.deepcopy(state_reward_func)
	directions = copy.deepcopy(state_reward_func)

	prob_suc = .7
	prob_opp = .2
	prob_sta = .1
	discount = .96

	utility_copy = copy.deepcopy(utility_func)

	for row in range(0,4):

		for col in range(0,4):

			print("index:", (4 * row) + col + 1)

			#init the udlr vals
			up = 0
			down = 0
			left = 0
			right = 0

			#check for bounds on top
			if( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
				up = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
					(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )
			#bounds on bottom
			elif( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
				up = ( utility_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
					(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]) )
			else:
				up = ( utility_func[row][col] + (prob_suc * utility_func[row - 1][col]) +
					(prob_opp * utility_func[row + 1][col]) + (prob_sta * utility_func[row][col]) )

			#check for bounds on bottom
			if( (row == 3 and col == 0) or (row == 3 and col == 1) or (row == 3 and col == 2) or (row == 3 and col == 3) ):
				down = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
					(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]) )
			#and bounds on top
			elif( (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 0 and col == 2) or (row == 0 and col == 3) ):
				down = ( utility_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
					(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
			else:
				down = ( utility_func[row][col] + (prob_suc * utility_func[row + 1][col]) +
					(prob_opp * utility_func[row - 1][col]) + (prob_sta * utility_func[row][col]))



			#check for bounds on left
			if( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
				left = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
					(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))
			#and then again on the right
			elif( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
				left = ( utility_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
					(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
			else:
				left = ( utility_func[row][col] + (prob_suc * utility_func[row][col - 1]) +
					(prob_opp * utility_func[row][col + 1]) + (prob_sta * utility_func[row][col]))

			#check for bounds on right
			if( (row == 0 and col == 3) or (row == 1 and col == 3) or (row == 2 and col == 3) or (row == 3 and col == 3) ):
				right = ( utility_func[row][col] + (prob_suc * utility_func[row][col]) +
					(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))
			#last time on the left
			elif( (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) ):
				right = ( utility_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
					(prob_opp * utility_func[row][col]) + (prob_sta * utility_func[row][col]))
			else:
				right = ( utility_func[row][col] + (prob_suc * utility_func[row][col + 1]) +
					(prob_opp * utility_func[row][col - 1]) + (prob_sta * utility_func[row][col]))

			vals = {"up": up, "down": down, "left": left, "right": right}
			print(vals)
			winner = max(vals.values())
			print("max utility found was:", winner)
			utility_copy[row][col] = winner
			winners = []
			for k,v in vals.items():
				if(v == winner):
					winners.append(k)
			print(winners)
			directions[row][col] = winners

	

part2()
