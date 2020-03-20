from gameplay.player import Player
from scripts.DSL import DSL
class Player1(Player):
        def __init__(self):
                pass

        def get_action(self, state):
                global DSL
                actions = state.available_moves()
        
                for a in actions:
                        if 2>=DSL.numberPositionsProgressedThisRoundColumn(state,5) and DSL.actionWinsColumn(state, a):
                                return a
                return actions[0]
                
