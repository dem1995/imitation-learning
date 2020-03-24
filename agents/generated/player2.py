from gameplay.player import Player
from scripts.DSL import DSL
class Player2(Player):
	def __init__(self):
		pass

	def get_action(self, state):
		global DSL
		actions = state.available_moves()
		for a in actions:
			if DSL.isStopAction(a) and 2!=0:
				return a
		return actions[0]