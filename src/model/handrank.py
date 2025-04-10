from enum import Enum

class Hand_Rank(Enum):
	HIGH_CARD = 1
	PAIR = 2
	TWO_PAIR = 3
	THREE_OF_A_KIND = 4
	STRAIGHT = 5
	FLUSH = 6
	FULL_HOUSE = 7
	FOUR_OF_A_KIND = 8
	STRAIGHT_FLUSH = 9

	def __lt__(self, other):
		'''
		Overload for < operator.  This compares with respect to high hand.
		'''
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Hand_Rank cannot be compared to Object: {self}, {other}')
		else:
			return self.value < other.value

	def __eq__(self, other):
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Hand_Rank cannot be compared to Object: {self}, {other}')
		else:
			return self.value == other.value

	def __gt__(self, other):
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Hand_Rank cannot be compared to Object: {self}, {other}')
		else:
			return self.value > other.value

	def __repr__(self):
		return self.name