from .suit import Suit
from .rank import Rank
from .card import Card
from itertools import product
import random

class Deck:
	'''
	Class for a Deck of cards.  This is a standard deck of 52 cards.
	'''
	def __init__(self, shuffled=True):
		self.cards = []
		for suit, rank in product(Suit, Rank):
			self.cards.append(Card(rank=rank, suit=suit))

		if shuffled:
			self.shuffle()

	def shuffle(self):
		if self.cards is None or len(self.cards) == 0:
			return
		random.shuffle(self.cards)

	def __repr__(self):
		s = ''
		for card in self.cards:
			s += f'{card}\n'
		return s

	def __len__(self):
		return len(self.cards)

	def deal(self):
		'''
		Function to simulate dealing a card.  Decreases deck size by 1.
		'''
		return self.cards.pop()