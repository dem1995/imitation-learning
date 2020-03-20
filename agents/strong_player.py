"""The best script after running the program with 26 epochs"""

#vigorous-crane
from collections import defaultdict
from gameplay.player import Player
from scripts.DSL import DSL

class StrongPlayer(Player):
	def __init__(self):
		self.name = 'vigorous-crane'

	def get_action(self, state):
		actions = state.available_moves()
        
		for a in actions:
			#return a
			if DSL.hasWonColumn(state,a) and DSL.isStopAction(a):
				return a
		return actions[0]