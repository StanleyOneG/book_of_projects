





import random
import sys

# Set up the constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

def get_bet(max_bet):
""" Ask the player how much money they want to bet """
    # Keep asking until the player enters the valid amount
    while True:
        print(f"How much do you want to bet? (from 1 to {max_bet} or QUIT)")
        bet = input('> ').upper().strip()

        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet # Player entered a valid bet

def get_deck():
""" Return a list of (rank, suit) tuples for all 52 cards in the deck."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numberd cards
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck

def display_hands(player_hand, dealer_hand, show_dealer_first):
""" Show the player's and dealer's hands. Hide dealer's first card if
show_dealer_first is False """
    pass

def main():
    print(''' Blackjack.

     Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money")
            print("Thanks for playing")
            sys.exit()

        # Let the player enter bet for this round
        print("Money: ", money)
        bet = get_bet(money)

        # Give dealer and player card from the deck each:
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions:


        break


if __name__ == '__main__':
    main()
