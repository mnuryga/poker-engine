from enum import Enum

class Rank(Enum):
	'''
	Rank ENUM.
	'''
	ACE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13

	def __lt__(self, other):
		'''
		Overload for < operator.  This compares with respect to high hand.
		'''
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Rank cannot be compared to Object: {self}, {other}')
		else:
			# if self card is an ACE, will never be less than other
			if self == self.ACE:
				return False

			# if other card is an ACE, will always be less than other
			if other == self.ACE:
				return True

			return self.value < other.value

	def __eq__(self, other):
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Rank cannot be compared to Object: {self}, {other}')
		else:
			return self.value == other.value

	def __gt__(self, other):
		if self.__class__ is not other.__class__:
			raise RuntimeError(f'Rank cannot be compared to Object: {self}, {other}')
		else:
			return self.value > other.value

	def __repr__(self):
		return self.name