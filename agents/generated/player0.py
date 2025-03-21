from gameplay.player import Player
from scripts.DSL import DSL
class Player0(Player):
	def __init__(self):
		pass

	def get_action(self, state):
		global DSL
		actions = state.available_moves()
	
		for a in actions:
			if DSL.hasWonColumn(state,a) and DSL.isStopAction(a):
				return a
		return actions[0]
		