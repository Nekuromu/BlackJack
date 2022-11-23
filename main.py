import random

card_deck = [
    {"Spade 2": 2},
    {"Spade 3": 3},
    {"Spade 4": 4},
    {"Spade 5": 5},
    {"Spade 6": 6},
    {"Spade 7": 7},
    {"Spade 8": 8},
    {"Spade 9": 9},
    {"Spade 10": 10},
    {"Spade Jack": 10},
    {"Spade Queen": 10},
    {"Spade King": 10},
    {"Spade Ace": 11},
    {"Diamond 2": 2},
    {"Diamond 3": 3},
    {"Diamond 4": 4},
    {"Diamond 5": 5},
    {"Diamond 6": 6},
    {"Diamond 7": 7},
    {"Diamond 8": 8},
    {"Diamond 9": 9},
    {"Diamond 10": 10},
    {"Diamond Jack": 10},
    {"Diamond Queen": 10},
    {"Diamond King": 10},
    {"Diamond Ace": 11},
    {"Clover 2": 2},
    {"Clover 3": 3},
    {"Clover 4": 4},
    {"Clover 5": 5},
    {"Clover 6": 6},
    {"Clover 7": 7},
    {"Clover 8": 8},
    {"Clover 9": 9},
    {"Clover 10": 10},
    {"Clover Jack": 10},
    {"Clover Queen": 10},
    {"Clover King": 10},
    {"Clover Ace": 11},
    {"Heart 2": 2},
    {"Heart 3": 3},
    {"Heart 4": 4},
    {"Heart 5": 5},
    {"Heart 6": 6},
    {"Heart 7": 7},
    {"Heart 8": 8},
    {"Heart 9": 9},
    {"Heart 10": 10},
    {"Heart Jack": 10},
    {"Heart Queen": 10},
    {"Heart King": 10},
    {"Heart Ace": 11},
]

discards_deck = []

player_bank = 1000
current_bet = 0

player_hand = []
dealer_hand = []


def shuffle_deck(_deck):
    """Will shuffle whatever deck (list) you give it."""
    random.shuffle(_deck)


def deal_card(_hand, _amount):
    """Pops the top cards from the list/deck and into the parameter's hand."""
    for i in range(_amount):
        _hand.append(card_deck.pop(0))


def bet(_bet):
    """Loops through and lets the player toss in chips until they are done betting."""
    done_betting = False
    while not done_betting:
        amount = int(input("How much do you bet? (1, 5, 25, 50, 100, 500)?\n"))
        _bet += amount
        print(f"You are betting: {_bet}.")
        if input("Done betting? y/n?\n") == "n":
            done_betting = False
        else:
            return _bet


def ask_double(_bet):
    if current_bet * 2 > player_bank:
        return
    else:
        if input("Would you like to double your bet? y/n?") == "y":
            _bet *= 2
        return _bet


def check_for_win(p_hand, d_hand):
    """Checks for game ending logic such as blackjacks, busts (both player and dealer). If nothing is found it will
    keep 'continue' for game variable. """
    amount = add_up_hand(p_hand)
    if amount > 21:
        return "bust."
    elif amount == 21:
        return "you win!"
    elif add_up_hand(d_hand) > 21:
        return "dealer bust."
    elif add_up_hand(d_hand) == 21:
        return "dealer wins."
    else:
        return "continue"


def add_up_hand(hand):
    """Adds up the value amount of a hand and returns it."""
    amount = 0
    for card in hand:
        for key in card:
            amount += card[key]
    return amount


def discard_cards(hand):
    for card in range(len(hand)):
        discards_deck.append(hand.pop(0))


game = "continue"
round = "continue"

shuffle_deck(card_deck)

while game == "continue":

    while round == "continue":

        print(f"You currently have {player_bank} in the bank.")
        current_bet = bet(current_bet)
        player_bank -= current_bet
        deal_card(player_hand, 2)
        round = check_for_win(player_hand, dealer_hand)
        if round != "continue":
            break
        print(f"You have {player_hand}. Amount:" + str(add_up_hand(player_hand)))
        deal_card(dealer_hand, 1)
        print(f"The dealer has {dealer_hand}. Amount:" + str(add_up_hand(dealer_hand)))
        # THIS IS WHERE DOUBLE GOES! (I think)
        while check_for_win(player_hand, dealer_hand) == "continue":
            if input("Hit or Stand? h/s?\n") == "h":  # HITTING!
                deal_card(player_hand, 1)
                print(f"HIT! You have {player_hand}. Amount:" + str(add_up_hand(player_hand)))
                round = check_for_win(player_hand, dealer_hand)
                if round != "continue":
                    break
            else:  # STANDING OR ELSE!
                deal_card(dealer_hand, 2)
                print(f"Stand. The dealer has {dealer_hand}. Amount:" + str(add_up_hand(dealer_hand)))
                round = check_for_win(player_hand, dealer_hand)
                if round != "continue":
                    break
    if round != "continue":
        print(round)
    if round == "you win!" or "dealer bust.":
        player_bank += (current_bet * 2)
    discard_cards(player_hand)
    discard_cards(dealer_hand)
    current_bet = 0
    if input("Ready for another round? y/n?\n") == "y":
        round = "continue"
    else:
        game = "quit"
