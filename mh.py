from gameplay.player import Player
from scripts.ScriptTree import ScriptTree
from config import Config
from agents.strong_player import StrongPlayer
from math import exp
import random
from pytools import argmin
from shutil import rmtree
from uuid import uuid4
import pickle

def distance(player:Player, trainingdata):
	"""
	Returns the distance between the given program's output and a "perfect" program
	"""
	incorrect = 0
	for game, action in trainingdata:
		if player.get_action(game)!=action:
			incorrect += 1
	return incorrect

# def sample(center:ScriptTree):
# 	return ScriptTree.Sample(center)


def metrohast(samplecount, trainingdata):
	# def computealpha(sampleprime, sample):
	# 	if sampleprime==0 and sample==0:
	# 		return 
	# 	elif sample == 0:
			

	sample = ScriptTree(identification=0)
	dist = distance(sample.player, trainingdata)
	samples = list()
	distances = list()

	while len(samples) < samplecount:

		# trims = [ ScriptTree.Sample(sample, uuid4().hex) for i in range(3)]
		# besttrim_i = argmin([distance(trim.player, trainingdata) for trim in trims])
		# sampleprime = ScriptTree(trims[besttrim_i].tree, f"{len(samples)}_{uuid4().hex}")
		bigchange = random.uniform(0, 1)<0.01
		startchange = random.uniform(0, 1)<0.01
		if bigchange:
			print("bigchange")
		elif startchange:
			print("start change")

		sampleprime = ScriptTree.Sample(sample, f"{len(samples)}{uuid4().hex}", bigchange, startchange)
		distprime = distance(sampleprime.player, trainingdata)

		if distprime == 0:
			improvement = 1
		else:
			improvement = exp(3*-dist/distprime)

		if random.uniform(0, 1) <= improvement:
			print("sample num", len(samples))
			print(distprime)
			#print(sampleprime.player.script)
			#sampleprime.save_image_to(Config.imagepath+ f"/tree{len(samples)}.png")
			samples.append(sampleprime)
			distances.append(distprime)
			sample = sampleprime
			dist = distprime
	return samples, distances



# def testdistance():
# 	samples = Config.LoadTrainingPairs()
# 	strongplayer = StrongPlayer()
# 	actions = list()
# 	for game, action in samples:
# 		chosenaction = strongplayer.get_action(game)
# 		gapair = (game, chosenaction)
# 		actions.append(gapair)
# 	dist = distance(strongplayer, actions)
# 	print(dist)



# def mh(samplecount, trainingset):

# 	sample = None #Todo- generate sample
# 	samples = list()

# 	while len(samples)<samplecount:
# 		sampleprime = generate_sample_about(sample) #todo - generate sample
# 		alpha = distance_function(sampleprime)/distance_function(sample)



# def sample(center:ScriptTree):
# 	sample = ScriptTree.sample(center)
# 	return generated_sample







# #Gets the distance of the sample from the ideal
# #distance_function(sample) is proportional to underlying_distribution(sample)
# #so d(x)/d(y) = u(x)/u(y)
# def distance_function(sample):
# 	distance = None
# 	#TODO
# 	return distance

if __name__ == "__main__":
	# # rmtree("./metrohast/__pycache__")
	trainingdata = Config.LoadTrainingPairs()
	print(len(trainingdata))
	samples, distances = metrohast(200, trainingdata)
	best = argmin(distances)
	print(best)
	print(distances)
	print(distances[best])
	print(samples[best].to_script())
	with open("intermediates/round1samples.pickle", 'wb') as outfile:
		pickle.dump([sample.to_script() for sample in samples], outfile)
	with open("intermediates/round1distances.pickle", 'wb') as outfile:
		pickle.dump(distances, outfile)
	# rmtree("./__pycache__")
	# rmtree("./scripts/__pycache__")
	# rmtree("./gameplay/__pycache__")
	# rmtree("./agents/__pycache__")
