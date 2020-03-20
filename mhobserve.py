import pickle
from agents.generated.player1 import Player1
from agents.generated.player2 import Player2
from agents.generated.player3 import Player3
from agents.generated.player4 import Player4
from mh import distance

# with open("intermediates/round1distances.pickle", 'rb') as infile:
# 	distances = pickle.load(infile)

# with open("intermediates/round1samples.pickle", 'rb') as infile:
# 	scripts = pickle.load(infile)


# indices = [i for i in range(len(distances)) if distances[i]<360]

# for i in indices:
# 	print(distances[i])
# 	print(scripts[i])
# 	print("--------------------------")

with open("intermediates/state_action_pairs.pickle", 'rb') as infile:
	pairs = pickle.load(infile)

print(len(pairs))
print(distance(Player1(), pairs))
print(distance(Player2(), pairs))
print(distance(Player3(), pairs))
print(distance(Player4(), pairs))
