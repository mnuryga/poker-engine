from model.deck import Deck
from model.hand import Hand
from model.rank import Rank

def main():
	# example code
	deck = Deck(shuffled=False)
	hand = Hand(deck.cards[9:14])

	print(hand)
	print(hand.is_flush)
	print(hand.is_straight)

	deck.shuffle()
	print(deck.deal())
	print(f'{len(deck) = }')

if __name__ == '__main__':
	main()