#Imitation Learning
##Overview
Takes a relatively strong AI agent and attempts to mimic that agent's behavior through imitation learning to achieve a relatively strong, explainable AI.

The program starts by generating input-output pairs using a UCT artificial intelligence agent. Those pairs are then used as part of a distance function from what is now the "ideal" program's results. The distance function is used to sample from an probability distribution favoring agents close to the "ideal" program in terms of results using the Manhattan-Hastings algorithm.

##How to run
Just run main.py. Python package requirements are given in the requirements.txt file.

Additional configuration can be done with the Config file.


##Examples
Example generated rules are given in the agents/generated folder
