from gameplay.player import Player
from scripts.DSL import DSL

class Player4(Player):
        def __init__(self):
                pass

        def get_action(self, state):
                global DSL
                actions = state.available_moves()
        
                for a in actions:
                        if DSL.actionWinsColumn(state, a) and DSL.numberPositionsConquered(state, 5)<=2:
                                return a
                return actions[0]