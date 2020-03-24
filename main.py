import os
from pytools import argmin

from agents.vanilla_uct_player import Vanilla_UCT
from gameplay.tournament import give_action_pairs
from config import Config
from mh import metrohast



def main():
	players = list()
	numfilters = 5

	#Generate input-output pairs to imitate
	Config.filtcount = 0
	generate_training_samples(numberpairs = 
	                          Config.num_original_training_samples)

	#While we haven't filtered the input-output pairs by learning new rules
	# enough times
	for i in range(numfilters):
		Config.filtcount = i
		#Generate the next "best" player for the current remaining
		# input-output pairs by sampling algorithms a bunch using 
		# Metropolis-Hastings
		players.append(metropolis_hastings_process())
		#Filter the samples using the generated player.
		filter_samples(players)
		
		
def metropolis_hastings_process():
	"""
	Samples a bunch of algorithms (with count specified in Config), saves their
	scores, and returns the best of the bunch.
	"""
	trainingdata = Config.LoadTrainingPairs()
	print(len(trainingdata))
	samples, distances = metrohast(Config.mh_samplecount, trainingdata)
	best = argmin(distances)
	print("Index of best player is ", best)
	print("Distances under distance metric:")
	print(distances)
	print("Best distance: ", distances[best])
	print("Best rule (along with script):")
	print(samples[best].to_script())
	print("------------------------------------------------------------------")
	Config.SaveDistances(distances)
	Config.SaveSamples([sample.to_script() for sample in samples])
	return samples[best].player


def generate_training_samples(numberpairs):
	"""
	Generates numberpairs training samples of game-action pairs using the 
	UCT players, c=1, and number of simulations defined in Config
	"""
	curpairs = list()
	uct1 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount)
	uct2 = Vanilla_UCT(c=1, n_simulations=Config.uct_simcount)

	pairs = give_action_pairs(uct1, uct2, numberpairs)
	curpairs.extend(pairs)

	Config.SaveTrainingPairs(curpairs)

def filter_samples(players):
	"""Filter the remaining training samples using the most recent rule"""
	player = players[Config.filtcount]

	samples = Config.LoadTrainingPairs()
	print("Results for filter number ", Config.filtcount)
	print("Number of samples before filtering:", len(samples))
	newsamples = list()
	for sample in samples:
		if player.get_action(sample[0])!=sample[1]:
			newsamples.append(sample)
	print("Number of samples after filtering: ", len(newsamples))
	Config.filtcount=Config.filtcount+1
	Config.SaveTrainingPairs(newsamples)

if __name__ == "__main__":
	response = input(f"Are you sure you want to potentially wipe whatever intermediates directory is specified by Config ({Config.intermediatespath}), and to start making new  files in that directory? Type y to continue doing so.")
	if response == 'y':
		if not os.path.exists(Config.intermediatespath):
			os.makedirs(Config.intermediatespath)
		main()
	else:
		print("You selected no. No files were wiped or created")