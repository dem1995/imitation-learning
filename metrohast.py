from gameplay.player import Player

def distance(player:Player, trainingdata):
	"""
	Returns the distance between the given program's output and a "perfect" program
	"""
	incorrect = 0
	for game, action in trainingdata:
		if player.get_action(game)!=action:
			incorrect += 1
	return incorrect

def generate_sample_about(center:ScriptTree):
	generated_sample = None
	#TODO
	return generated_sample


def mh(samplecount, trainingset):

	sample = None #Todo- generate sample
	samples = list()

	while len(samples)<samplecount:
		sampleprime = generate_sample_about(sample) #todo - generate sample
		alpha = distance_function(sampleprime)/distance_function(sample)




#Gets the distance of the sample from the ideal
#distance_function(sample) is proportional to underlying_distribution(sample)
#so d(x)/d(y) = u(x)/u(y)
def distance_function(sample):
	distance = None
	#TODO
	return distance

