
from enum import Enum, auto
from collections import defaultdict
from indexedproperty import indexedproperty
import random
from anytree import NodeMixin, PreOrderIter
from copy import deepcopy
from anytree.exporter import DotExporter
from anytree import RenderTree
from uuid import uuid4

class Grammar:
	class Tokens(Enum):
		START = 1,
		ANDEXPR2 = 20,
		ANDEXPR3 = 21,
		BOOL = 2,
		STBOOL = 3,
		SMALLNUM_COMP = 4
	
	class Semiterminals(Enum):
		INEQSYM = 5,
		SMALLNUM = 6,
		NUMBER = 7

	class Functions(Enum):
		IsDoubles = 10,
		ContainsNumber = 11,
		ActionWinsColumn = 12,
		NumberPositionsProgressedThisRoundColumn = 13,
		NumberPositionsConquered = 14,
		HasWonColumn = 15,
		IsStopAction = 16

	transitions = defaultdict(lambda: None)
	
	transitions[Tokens.START] = [[Tokens.BOOL], [Tokens.ANDEXPR2]]
	#[Tokens.ANDEXPR3]]
	transitions[Tokens.ANDEXPR2] = [[Tokens.BOOL, Tokens.BOOL]]
	transitions[Tokens.ANDEXPR3] = [[Tokens.BOOL, Tokens.BOOL, Tokens.BOOL]]
	transitions[Tokens.BOOL] = [[Tokens.SMALLNUM_COMP], [Tokens.STBOOL]]
	transitions[Tokens.SMALLNUM_COMP] = [[Semiterminals.SMALLNUM, Semiterminals.INEQSYM, Semiterminals.SMALLNUM]]
	transitions[Tokens.STBOOL] = [[Functions.IsDoubles], [Functions.ContainsNumber], [Functions.ActionWinsColumn], [Functions.HasWonColumn], [Functions.IsStopAction]]

	transitions[Semiterminals.SMALLNUM] = [['0'], ['1'], ['2'], 
		[Functions.NumberPositionsConquered], 
		[Functions.NumberPositionsProgressedThisRoundColumn]]
	transitions[Semiterminals.INEQSYM] = [['<'], ['<='], ['=='], ['>='], ['>'], ['!=']]
	transitions[Semiterminals.NUMBER] = [['2'], ['3'], ['4'], ['5']]

	transitions[Functions.IsDoubles] = [['DSL.isDoubles(a)']]
	transitions[Functions.ContainsNumber] = [['DSL.containsNumber(a, {0})', Semiterminals.NUMBER]]
	transitions[Functions.ActionWinsColumn] = [['DSL.actionWinsColumn(state, a)']]
	transitions[Functions.HasWonColumn] = [['DSL.hasWonColumn(state,a)']]
	transitions[Functions.NumberPositionsProgressedThisRoundColumn] = [['DSL.numberPositionsProgressedThisRoundColumn(state,{0})', Semiterminals.NUMBER]]
	transitions[Functions.IsStopAction] = [['DSL.isStopAction(a)']]
	transitions[Functions.NumberPositionsConquered] = [['DSL.numberPositionsConquered(state, {0})', Semiterminals.NUMBER]]


class ScriptNode(NodeMixin):
	def __init__(self, symbol, parent=None, children = None):
		super(ScriptNode, self).__init__()
		self.symbol = symbol
		self.parent = parent
		self.display_name = self.symbol if isinstance(self.symbol, str) else self.symbol.name
		self.name = self.display_name + uuid4().hex
		
		if children:
			self.children = children
			
	def scriptstr(self):
		#Token consideration
		if self.symbol in [Grammar.Tokens.START, Grammar.Tokens.BOOL, Grammar.Tokens.STBOOL]:
			#print("in first block")
			#print(self.children[0].symbol)
			return self.children[0].scriptstr()
		elif self.symbol in [Grammar.Tokens.ANDEXPR2, Grammar.Tokens.ANDEXPR3]:
			# lhs = self.children[0].scriptstr()
			# rhs = self.children[1].scriptstr()
			return " and ".join([child.scriptstr() for child in self.children])
		elif self.symbol == Grammar.Tokens.SMALLNUM_COMP:
			lhs = self.children[0].scriptstr()
			center = self.children[1].scriptstr()
			rhs = self.children[2].scriptstr()
			return lhs + center + rhs
		#Semiterminal consideration
		elif self.symbol in list(Grammar.Semiterminals):
			if isinstance(self.children[0].symbol, str):
				return self.children[0].symbol
			else:
				return self.children[0].scriptstr()
		#Function consideration
		elif self.symbol in list(Grammar.Functions):
			funcstring = self.children[0].scriptstr()
			params = [param.scriptstr() for param in self.children[1:]]
			return funcstring.format(*params)
		elif isinstance(self.symbol, str):
			return self.symbol
		#print(self.symbol)
		return "whattt"

	def semiterminals(self):
		traversal = PreOrderIter(self)
		mutablenodes = [node for node in traversal 
		                if node.symbol in list(Grammar.Semiterminals)
					    	or node.symbol == Grammar.Tokens.STBOOL]
		return mutablenodes
	
	def mutable_tokens(self):
		traversal = PreOrderIter(self)
		mutablenodes = [node for node in traversal 
		                if node.symbol in [Grammar.Tokens.BOOL]]
		return mutablenodes

	@staticmethod
	def RandomDerivation(node = None, forbiddentoroot=[]):
		node = deepcopy(node)

		if node is None:
			node = ScriptNode(Grammar.Tokens.START)
		
		transition_possibilities = Grammar.transitions[node.symbol]
		if not transition_possibilities is None:
			transition_possibilities=[transition for transition in Grammar.transitions[node.symbol] if not transition in forbiddentoroot]

		if not transition_possibilities is None:
			children = random.choice(transition_possibilities) 
			children = [ScriptNode(child) for child in children]

			for child in children:
				child = ScriptNode.RandomDerivation(child)
				child.parent = node
		return node
	
class ScriptTree:
	def __init__(self, tree=None, identification="NoID"):
		"""dts"""
		self.tree = tree or ScriptNode.RandomDerivation()
		self.id = identification
		def makeClass(scripttree:ScriptTree):
			exec(scripttree.to_script())
			return eval(f'Player{scripttree.id}')
		self.player = makeClass(self)()
		self.player.script = self.to_script()
		

	def save_image_to(self, location):
		DotExporter(self.tree, nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name)).to_picture(location)

	def to_script(self):
		retstr =\
f'''
from gameplay.player import Player
from scripts.DSL import DSL

class Player{self.id}(Player):
	def __init__(self):
		pass

	def get_action(self, state):
		global DSL
		actions = state.available_moves()
        
		for a in actions:
			if {self.tree.scriptstr()}:
				return a
		return actions[0]
'''
		return retstr
	
	def print(self):
		for pre, fill, node in RenderTree(self.tree):
			print("%s%s" % (pre, node.display_name))

	@staticmethod 
	def Sample(center, identification = "NoID", bigmutate=False, startmutate=False):
		#center.print()
		centerrootcopy = deepcopy(center.tree)
		if bigmutate:
			nodetomutate = random.choice(centerrootcopy.mutable_tokens())
		elif startmutate:
			nodetomutate = centerrootcopy.root
		else:
			nodetomutate = random.choice(centerrootcopy.semiterminals())
		
		previous_transition = [child.symbol for child in nodetomutate.children]
		#Remove a subtree of a semiterminal
		#print("Node to mutate", nodetomutate.symbol)
		for mutatednodechild in nodetomutate.children:
			mutatednodechild.parent = None
		nodetomutate.children = []

		#Randomly regenerate that subtree
		mutation = ScriptNode.RandomDerivation(nodetomutate, forbiddentoroot=[previous_transition])
		for mutatednodechild in mutation.children:
			mutatednodechild.parent = nodetomutate
		mutatedtree = ScriptTree(centerrootcopy, identification=identification)
		#mutatedtree.print()
		return mutatedtree

		

