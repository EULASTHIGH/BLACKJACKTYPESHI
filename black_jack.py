import random

class card:

    def __init__(self, suit , rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class deck:
    
    def __init__(self):
        self.cards = []
        suites = ["spades" , "clubs" , "hearts" , "diamonds"]
        ranks = [
        {"rank": "A", "value": 11},
        {"rank": "2", "value": 2},
        {"rank": "3", "value": 3},
        {"rank": "4", "value": 4},
        {"rank": "5", "value": 5},
        {"rank": "6", "value": 6},
        {"rank": "7", "value": 7},
        {"rank": "8", "value": 8},
        {"rank": "9", "value": 9},
        {"rank": "10", "value": 10},
        {"rank": "J", "value": 10},
        {"rank": "Q", "value": 10},
        {"rank": "K", "value": 10},
                ]
        for suit in suites: 
            for rank in ranks:
                self.cards.append(card(suit, rank))

    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self,number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards)>0 : 
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class hand:

    def __init__(self, dealer = False):
        self.cardss = []
        self.value = 0
        self.dealer = dealer

    def add_cards(self, card_list):
        self.cardss.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cardss:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        
        if has_ace and self.value > 21 :
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21 
    
    def display(self,show_all_dealer_Cards = False) :
        print(f'''{"Dealer's" if self.dealer else "your"} hand : ''')
        for index, card in enumerate(self.cardss):
            if index == 0 and self.dealer and not show_all_dealer_Cards:
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("value :" ,self.get_value())
        print()

class game:
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play\n:- "))
            except ValueError:
                print("please enter a number.")
    
        while game_number < games_to_play:
            game_number += 1
            
            game_deck = deck()
            game_deck.shuffle()

            
            player_Hand = hand()
            dealer_hand = hand(dealer = True)
            
            for i in range(2):
                player_Hand.add_cards(game_deck.deal(1))
                dealer_hand.add_cards(game_deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_Hand.display()
            dealer_hand.display()

            if self.check_winner(player_Hand, dealer_hand):
                continue
            
            choice = ""
            while player_Hand.get_value() < 21 and choice not in ["s" , "stand"]: 
                choice = input("please choose 'hit' or 'Stand': ").lower()
                while choice not in ["h" , "s" , "hit" , "stand"]:
                    choice = input("please enter 'Hit' or 'stand' (or H/S)").lower()
                if choice in ["hit" , "h"]:
                    player_Hand.add_cards(game_deck.deal(1))
                    player_Hand.display()

            if self.check_winner(player_Hand, dealer_hand):
                continue        
            
            player_Hand_value = player_Hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value <17:
                dealer_hand.add_cards(game_deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer_Cards=True)
            if self.check_winner(player_Hand, dealer_hand):
                continue 

            print("Final results")
            print("your hand:", player_Hand_value)
            print("dealer's hand:" , dealer_hand_value)

            self.check_winner(player_Hand,dealer_hand, True)

        print("\nThanks for playing!")

    def check_winner(self , player_hand , dealer_hand , game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("you busted. dealer wins! :(")
                return True
            elif dealer_hand.get_value()> 21:
                print("Dealer busted, you win! :)")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackajack! Tie! :0")
                return True
            elif player_hand.is_blackjack():
                print("you have blackjack. you win! :)")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("you win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie!")
            else:
                print("dealer wins!")
            return True
        return False

game_ = game()
game_.play()
