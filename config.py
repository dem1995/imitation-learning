import pickle

class Config:
	filtcount = 0

	@classmethod
	def trainingpath(cls, filtcount):
		return "intermediates/state_action_pairs_filtcount_{0}.pickle".format(filtcount)

	@classmethod
	def distancespath(cls, filtcount):
		return "intermediates/distances_filtcount_{0}.pickle".format(filtcount)

	@classmethod
	def samplespath(cls, filtcount):
		return "intermediates/samples_filtcount_{0}.pickle".format(filtcount)


	imagepath = "intermediates/images"
	uct_simcount = 150

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