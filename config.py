import pickle

class Config:
	trainingpath = "intermediates/state_action_pairs.pickle"
	imagepath = "intermediates/images"
	uct_simcount = 100

	@classmethod
	def LoadTrainingPairs(cls):
		with open(cls.trainingpath, 'rb') as infile:
			pairs = pickle.load(infile)
		return pairs

