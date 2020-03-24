from gameplay.player import Player
from scripts.DSL import DSL
class Player3(Player):
	def __init__(self):
		pass

	def get_action(self, state):
		global DSL
		actions = state.available_moves()

		for a in actions:
			if 0==0 and DSL.containsNumber(a, 5):
				return a
		return actions[0]
