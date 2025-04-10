from dataclasses import dataclass
from enum import Enum
from .suit import Suit
from .rank import Rank

@dataclass(frozen = True)
class Card:
	'''
	Card class.  Each Card will always have a rank and suit.
	'''
	rank: Rank
	suit: Suit

	def __lt__(self, other):
		'''
		Overload for < operator.  This compares with respect to high hand.
		'''
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Card comparison error: {self}, {other}')
		else:
			# this comparison considers ACEs as high
			return self.rank < other.rank

	def __eq__(self, other):
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Card comparison error: {self}, {other}')
		else:
			return self.rank == other.rank

	def __repr__(self):
		return f'{self.rank} of {self.suit}'