import pickle

class Config:
	filtcount = 0
	num_original_training_samples = 2000
	intermediatespath = "intermediates_new"
	imagepath = f"{intermediatespath}/images"
	uct_simcount = 150 #15 #150
	mh_samplecount = 450 #30 #450

	@classmethod
	def trainingpath(cls, filtcount):
		return f"{cls.intermediatespath}/state_action_pairs_filtcount_{cls.filtcount}.pickle"

	@classmethod
	def distancespath(cls, filtcount):
		return f"{cls.intermediatespath}/distances_filtcount_{cls.filtcount}.pickle"

	@classmethod
	def samplespath(cls, filtcount):
		return f"{cls.intermediatespath}/samples_filtcount_{cls.filtcount}.pickle"


	@classmethod
	def LoadTrainingPairs(cls):
		path = cls.trainingpath(cls.filtcount)
		with open(path, 'rb') as infile:
			pairs = pickle.load(infile)
		return pairs
	
	@classmethod
	def SaveTrainingPairs(cls, trainingpairs):
		path = cls.trainingpath(cls.filtcount)
		with open(path, 'wb') as outfile:
			pickle.dump(trainingpairs, outfile)

	@classmethod
	def LoadSamples(cls):
		path = cls.samplespath(cls.filtcount)
		with open(path, 'rb') as infile:
			pairs = pickle.load(infile)
		return pairs
	
	@classmethod
	def SaveSamples(cls, trainingpairs):
		path = cls.samplespath(cls.filtcount)
		with open(path, 'wb') as outfile:
			pickle.dump(trainingpairs, outfile)

	@classmethod
	def LoadDistances(cls):
		path = cls.distancespath(cls.filtcount)
		with open(path, 'rb') as infile:
			pairs = pickle.load(infile)
		return pairs
	
	@classmethod
	def SaveDistances(cls, trainingpairs):
		path = cls.distancespath(cls.filtcount)
		with open(path, 'wb') as outfile:
			pickle.dump(trainingpairs, outfile)