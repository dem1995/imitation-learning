from agents.generated.player0 import Player0
from agents.cumulative_player import CumulativePlayer
from gameplay.tournament import relative_performance

player1= Player0()
player2 = CumulativePlayer()



print(relative_performance(player1, player2, 1000))