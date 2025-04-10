from model.hand import Hand
from model.handrank import Hand_Rank

class Evaluator:
	'''
	Class to handle evaluation and scoring of hands.
	'''
	def __init__(self):
		pass

	@staticmethod
	def rank(hand):
		if len(hand) != 5:
			raise NotImplementedError('Cannot evaluate hands of nonstandard size')