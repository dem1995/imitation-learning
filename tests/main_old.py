from config import Config
from gameplay.tournament import give_action_pairs, play_game, relative_performance
from gameplay.tournament_old import PlayGamesBothSides
from agents.vanilla_uct_player import Vanilla_UCT
from agents.random_player import RandomPlayer
from scripts.ScriptTree import ScriptTree, ScriptNode
#from metrohast import distance
import time
import pickle

# def printsequence(sequence):
# 	for sequenceitem in sequence:
# 		print(sequenceitem)

# def main():
# 	#generate_and_store_training_samples()
# 	training_samples = Config.LoadTrainingPairs()


# def testmain():
# 	# agent1 = ScriptTree(identification=0)
	
# 	uct1 = Vanilla_UCT(c=1, n_simulations=10)
# 	uct2 = Vanilla_UCT(c=1, n_simulations=5)
# 	# print(agent1.to_script())
# 	start_time = time.time()
# 	print(PlayGamesBothSides(uct1, uct2, numgames=200))
# 	print("time", time.time()-start_time)
# 	start_time=time.time()
# 	print(relative_performance(uct1, uct2, num_games=200))
# 	print("time", time.time()-start_time)

def generate_and_store_training_samples():
	curpairs = Config.LoadTrainingPairs()
	uct1 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount)
	uct2 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount)

	pairs = give_action_pairs(uct1, uct2, numberpairs=2000)
	curpairs.extend(pairs)

	Config.SaveTrainingPairs(curpairs)

# def test_training_samples():
# 	uct1 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount)
# 	training_samples = Config.LoadTrainingPairs()
# 	print(distance(uct1, training_samples)

if __name__ == "__main__":
	generate_and_store_training_samples()