from agents.vanilla_uct_player import Vanilla_UCT
from gameplay.tournament import play_game, relative_performance, play_game_both_sides, give_action_pairs
from gameplay.game import Game
from statistics import mean
import elementally as elmy
import scripts.ScriptTree
from scripts.ScriptTree import ScriptTree, ScriptNode
from scripts.DSL import DSL
import pickle

import time



# uct1 = Vanilla_UCT(c=1, n_simulations=150)
# uct2 = Vanilla_UCT(c=1, n_simulations=5)


# game = Game(n_players = 2, dice_number = 4, dice_value = 3, column_range = [2,6],
# 			offset = 2, initial_height = 1)



print ("asga{0}, {1}s".format(*[1, 2]))
# results1 = list()



# # print("--- %s seconds ---" % (time.time() - start_time))

# print(scripts.ScriptTree.Grammar._grammar)

# pairs = give_action_pairs(uct1, uct1, 1000)
# with open("intermediates/state_action_pairs.pickle", 'wb') as outfile:
# 	pickle.dump(pairs, outfile)

with open("intermediates/state_action_pairs.pickle", 'rb') as infile:
	pairs = pickle.load(infile)


st = ScriptTree(ScriptNode.RandomDerivation())
st.print()
for semiterminal in st.tree.semiterminals():
	print(semiterminal.display_name)


st2 = ScriptTree.Sample(st)
st2.print()



print(len(pairs))
# for pair in pairs:
# 	print(pair)
id = 11324


# def makeClass(scripttree:ScriptTree):
# 	exec(scripttree.to_script())
# 	return eval(f'Player{scripttree.id}')

# score = -1
# identification =0
# while score < 0.15:
# 	start_time = time.time()
# 	st = ScriptTree(identification=identification)
# 	print(st.to_script())
# 	print(st.semiterminals)
# 	#st.save_image_to(f"images/tree{identification}.png")

# 	player = st.player

# 	results = relative_performance(uct1, player, 40)
# 	score = results[1]

# 	print(results)
# 	identification+=1
# 	print(time.time()-start_time)