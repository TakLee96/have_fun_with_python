from random import randint

def game_start():
	num_cookies = 10
	game_end = False
	player = 0
	print("Game Start! There are {0} cookies.".format(num_cookies))

	def take(num):
		nonlocal num_cookies, player, game_end
		if game_end:
			print("Game has ended!")
		else:
			if num_cookies < num:
				print("You cannot take {0} from {1} cookies".format(num, num_cookies))
			elif not 0 < num < 4:
				print("You can only take 1 to 3 cookies a time")
			else:
				print("You take {0} cookies".format(num))
				num_cookies -= num
				print("There is {0} cookies left".format(num_cookies))
				if num_cookies == 0:
					print("Player {0} wins".format(player))
					game_end = True
				if player == 1:
					strategy(num)
				player = 1 - player

	def strategy(num):
		nonlocal num_cookies, game_end
		if num_cookies == 0:
			print("You win!!!")
			game_end = True
		elif 0 < num_cookies < 4:
			print("Computer takes {0} cookies\nComputer wins!!!".format(num_cookies))
			game_end = True
		else:
			num_take = randint(1, 3)
			print("Computer takes {0} cookies".format(num_take))
			num_cookies -= num_take
			print("There is {0} cookies left".format(num_cookies))
			rand = randint(1, 2)
			print("Somebody brings {0} cookies".format(rand))
			num_cookies += rand
			print("There is {0} cookies left".format(num_cookies))

	game_start.take = take

def take(num):
	game_start.take(num)
