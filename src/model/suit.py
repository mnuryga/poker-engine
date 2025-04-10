from enum import Enum

class Suit(Enum):
	'''
	Suit ENUM.
	'''
	CLUBS = 1
	HEARTS = 2
	DIAMONDS = 3
	SPADES = 4

	def __hash__(self):
		return self.value

	def __eq__(self, other):
		if self.__class__ is not other.__class__:
			raise TypeError(f'Suit cannot be compared to Object: {self}, {other}')
		else:
			return self.value == other.value

	def __repr__(self):
		return self.name

	def __lt__(self):
		raise NotImplementedError('Suit should only be compared using equality')