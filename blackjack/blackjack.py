





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

def get_hand_value(cards):
    """ Returns the value of cards. Face cards are worth 10,
    aces are worth 11 or 1 (function picks the most suitable value)"""
    value = 0
    num_of_aces = 0

    # Add value for non-ace cards:
    for card in cards: # cards is a tuple (rank, suit)
        rank = card[0]
        if rank == 'A':
            num_of_aces += 1
        elif rank in ('J', 'K', 'Q'): # Face cards are worth 10
            value += 10
        else:
            value += int(rank)

    # Add value for aces:
    value += num_of_aces # Add 1 per ace
    # If another 10 can be added, do so:
    for i in range(num_of_aces):
        if value + 10 <= 21:
            value += 10

    return value

def display_cards(cards):
    """ Didplsy all the cards in cards list """
    rows = ['', '', '', '', ''] # The text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___  ' # Print the top line of the card
        if card == BACKSIDE:
            # Print the card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # print the card's front:
            rank, suit = card # unpack a tuple
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f"|_{rank.rjust(2, '_')}| "
    # Print each row in the screen
    for row in rows:
        print(row)

def display_hands(player_hand, dealer_hand, show_dealer_first):
    """ Show the player's and dealer's hands. Hide dealer's first card if
    show_dealer_first is False """
    if show_dealer_first:
        print('DEALER: ', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        # Hide dealer's first card
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards
    print('PLAYER: ', get_hand_value(player_hand))
    display_cards(player_hand)

def get_move(player_hand, money):
    """ Asks the player for their move, and returns H for hit, S for stand,
    and D for double down"""
    while True: # Keep looping until the player enters correct move
        # Determine what move the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down in their first move
        # the first move is when their have only two cards
        if len(moves) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        move_choice = '\n'.join(moves) + '\n > '
        move = input(move_choice).upper()
        if move in ('H', 'S'):
            return move # The player has entered correct move
        if move == 'D' and '(D)ouble down' in moves:
            return move # The player has entered correct move

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
        print('Bet: ', bet)
        while True: # Keep looping until the player stands or bust
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust:
            if get_hand_value(player_hand) >21:
                print('Unfortunately, you ran out of 21...')
                break
            
            # Get the player's move, either H, S, or D:
            move = get_move(player_hand, money - bet)

            # Handle the player's move
            if move == 'D':
                # The player is doubling down:
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f'Bet increased to {bet}')
                print('Bet: ', bet)

            if move in ('H', 'D'):
                # Hit/Doubling down takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # The player has busted
                    print('You have more than 21...')
                    continue

            if move in ('S', 'D'):
                # Stand/Doubling down stops the player's turn
                break

        # Handle the dealer's action:
        if get_hand_value(player_hand) < 21:
            while get_hand_value(dealer_hand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break # The dealer has busted
                input('Press enter to continue...')
                print('\n\n')

        # Show the final hands:
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        # Handle whether the player won, lost or tied:
        if dealer_value > 21:
            print(f'Dealer bust! you win {bet}')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won {bet}!')
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


if __name__ == '__main__':
    main()
