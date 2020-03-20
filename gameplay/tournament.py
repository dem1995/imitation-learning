import elementally as elmy
from gameplay.game import Game
from agents.random_player import RandomPlayer
from copy import deepcopy

def relative_performance(player1, player2, num_games, max_moves = 200):
	"""
	Plays multiple games of Can't-Stop between players
	"""
	rungame = lambda: play_game_both_sides(player1, player2, max_moves)
	games_results = [rungame() for _ in range(num_games//2)]
	#print(games_results)
	results_sum = elmy.sum(*games_results)
	#print(results_sum)
	results_average = tuple(entry/(num_games//2) for entry in results_sum)
	#print(results_average)
	return results_average

def play_game_both_sides(player1, player2, max_moves = 200):
	results1 = play_game(player1, player2, max_moves)
	results2 = reversed(play_game(player2, player1, max_moves))

	results = elmy.sum(results1, results2)
	results = tuple(result/2 for result in results)
	return results

def give_action_pairs(player1, player2, numberpairs, max_moves = 200):
	state_action_pairs_all = list()

	while len(state_action_pairs_all) < numberpairs:
		results, state_action_pairs = play_game_and_give_action_pairs(player1, player2, max_moves)
		state_action_pairs_all.extend(state_action_pairs)

	return state_action_pairs_all[:numberpairs]


def play_game(player1, player2, max_moves = 200):
	"""
	Plays a game of Can't-Stop between the given players

	Returns (-1, -1) if max_moves has been exceeded. Returns (1, 0) if player 1 wins, and returns (0, 1) if player 2 wins.
	"""
	results, state_action_pairs = play_game_and_give_action_pairs(player1, player2, max_moves)
	return results
	
	
def play_game_and_give_action_pairs(player1, player2, max_moves = 200):
	"""
	Plays a game of Can't-Stop between the given players

	Returns (-1, -1) if max_moves has been exceeded. Returns (1, 0) if player 1 wins, and returns (0, 1) if player 2 wins.
	"""

	state_action_pairs = list()

	#Create the game
	game = Game(n_players = 2, dice_number = 4, dice_value = 3, column_range = [2,6],
				offset = 2, initial_height = 1)
	current_player = game.player_turn

	
	#Cycle through the game until it concludes, or until a move count limit has been reached
	who_won = None
	move_count = 0
	is_over = False
	while not is_over:
		moves = game.available_moves()
		#Progress the game to the next player's turn if a player has busted
		if game.is_player_busted(moves):
			current_player = 2 if current_player==1 else 1
			continue
		#Otherwise, we're in the middle of a turn
		else:
			#Get the current player's action and play it
			play_chooser = player1 if game.player_turn == 1 else player2
			chosen_play = play_chooser.get_action(game)
			state_action_pairs.append((deepcopy(game), deepcopy(chosen_play)))
			game.play(chosen_play)
			move_count += 1
			#if the player chooses to conclude their turn prior to busting, progress the game
			if chosen_play == 'n':
				current_player = 2 if current_player==1 else 1
		#Get whether the game has concluded, as well as the current standings
		who_won, is_over = game.is_finished()
		
		if move_count > max_moves:
			is_over = True
			who_won = -1
	
	#Get the final scores
	#print("who won", who_won)
	if who_won == -1:
		final_scores = (0, 0)
	else:
		final_scores = (1, 0) if who_won==1 else (0, 1)

	return final_scores, state_action_pairs