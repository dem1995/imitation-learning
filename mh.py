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

def metrohast(samplecount, trainingdata):
	"""
	Uses the metropolis-hastings algorithm to collect program samples
	"""
	
	#Create a starting sample (not actually added to the sample list)
	#Also createa list of samples and distances from those samples to an
	#  ideal replicating program
	sample = ScriptTree(identification=0)
	dist = distance(sample.player, trainingdata)
	samples = list()
	distances = list()

	#Until we've generated the desired number of samples, repeat the
	#  Metropolis-hastings sampling/acceptance loop
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

		# if distprime == 0:
		# 	improvement = 1
		# else:
		# 	improvement = exp(3*-distprime/dist)
		if distprime == 0:
			improvement = 1
		else:
			improvement = min([1, dist/distprime])

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