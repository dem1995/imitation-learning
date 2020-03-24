from agents.generated.player0 import Player0
from agents.generated.player1 import Player1
from agents.generated.player2 import Player2
from agents.generated.player3 import Player3
from config import Config


Config.filtcount=2
players = [Player0(), Player1(), Player2(), Player3()]
player = players[Config.filtcount]

samples = Config.LoadTrainingPairs()
print(len(samples))
newsamples = list()
for sample in samples:
	if player.get_action(sample[0])!=sample[1]:
		newsamples.append(sample)
print(len(newsamples))
Config.filtcount = Config.filtcount+1
Config.SaveTrainingPairs(newsamples)
