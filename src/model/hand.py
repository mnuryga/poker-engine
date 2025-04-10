from .suit import Suit
from .rank import Rank
from .card import Card

class Hand:
	'''
	Class for a Hand of cards.
	'''
	def __init__(self, cards):
		self.cards = cards

	@property
	def is_flush(self):
		'''
		Whether or not the hand is a flush.
		'''
		if len(self.cards) != 5:
			# todo: implement for nonstandard hand sizes
			raise NotImplementedError('Cannot determine for nonstandard hand sizes')

		suits = [card.suit for card in self.cards]
		return len(set(suits)) <= 1

	@property
	def is_straight(self):
		'''
		Whether or not the hand is a straight.
		'''
		if len(self.cards) != 5:
			# todo: implement for nonstandard hand sizes
			raise NotImplementedError('Cannot determine for nonstandard hand sizes')

		ranks = sorted([card.rank.value for card in self.cards])

		# if there is an ACE, check for broadway
		if 1 in ranks:
			# ACE will always be at bottom of sorted list
			top = ranks[1:]
			top.append(14)
			if max(top) - min(top) == len(top) - 1:
				return True

		return max(ranks) - min(ranks) == len(ranks) - 1

	def __repr__(self):
		s = ''
		for card in self.cards:
			s += f'{card}\n'
		return s

	def __len__(self):
		len(self.cards)