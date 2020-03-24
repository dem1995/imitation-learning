from config import Config
from gameplay.tournament import give_action_pairs
from agents.vanilla_uct_player import Vanilla_UCT
uct1 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount-75)
uct2 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount-75)

pairs = give_action_pairs(uct1, uct2, numberpairs=2000)
Config.filtcount=0
Config.SaveTrainingPairs(pairs)