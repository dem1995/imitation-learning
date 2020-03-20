import pickle

class Config:
	trainingpath = "intermediates/state_action_pairs.pickle"
	imagepath = "intermediates/images"
	uct_simcount = 150

	@classmethod
	def LoadTrainingPairs(cls):
		with open(cls.trainingpath, 'rb') as infile:
			pairs = pickle.load(infile)
		return pairs
	
	@classmethod
	def SaveTrainingPairs(cls, trainingpairs):
		with open(cls.trainingpath, 'wb') as outfile:
			pickle.dump(trainingpairs, outfile)