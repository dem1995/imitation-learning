from gameplay.player import Player
def distance(player:Player, trainingdata):
	"""
	Returns the distance between the given program's output and a "perfect" program
	"""
	incorrect = 0
	for game, action in trainingdata:
		if player.get_action(game)!=action:
			incorrect += 1
	return incorrect

