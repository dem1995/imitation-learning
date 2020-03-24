from gameplay.player import Player
from scripts.DSL import DSL
class CumulativePlayer(Player):
	def __init__(self):
		pass

	def get_action(self, state):
		actions = state.available_moves()
		#Rule r1
		for a in actions:
			if DSL.hasWonColumn(state,a) and DSL.isStopAction(a):
				return a
		#Rule r2
		for a in actions:
			if DSL.containsNumber(a, 4):
				return a
		#Rule r3
		for a in actions:
			if DSL.isStopAction(a) and DSL.isStopAction(a):
				return a
		#Rule r4
		for a in actions:
			if 0==0 and DSL.containsNumber(a, 5):
				return a
		#Rule r5
		for a in actions:
			if 2>=0 and DSL.containsNumber(a, 3):
				return a

		return actions[0]
	