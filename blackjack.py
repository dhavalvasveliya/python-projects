import random

class Blackjack:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.dealer_hand = []

    def create_deck(self):
        for suit in ['H', 'D', 'C', 'S']:
            for value in range(2, 11):
                self.deck.append(str(value) + suit)
            for face_card in ['J', 'Q', 'K', 'A']:
                self.deck.append(face_card + suit)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        self.hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        self.hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())

    def calculate_hand(self, cards):
        total = 0
        aces = 0
        for card in cards:
            if card[0].isdigit():
                total += int(card[0])
            elif card[0] == 'A':
                aces += 1
                total += 11
            else:
                total += 10
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def print_hand(self, cards, hide_dealer_card=False):
        print("\n")
        for i, card in enumerate(cards):
            if i == 0 and hide_dealer_card:
                print("X")
            else:
                print(card)
        print("Total:", self.calculate_hand(cards))

    def hit(self, cards):
        cards.append(self.deck.pop())

    def play_game(self):
        self.create_deck()
        self.shuffle_deck()
        self.deal_cards()
        self.print_hand(self.hand)
        while self.calculate_hand(self.hand) < 21:
            decision = input("Do you want to hit or stand? (h/s) ")
            if decision == 'h':
                self.hit(self.hand)
                self.print_hand(self.hand)
            elif decision == 's':
                break
        player_total = self.calculate_hand(self.hand)
        if player_total > 21:
            print("Busted!")
        else:
            self.print_hand(self.dealer_hand)
            while self.calculate_hand(self.dealer_hand) < 17:
                self.hit(self.dealer_hand)
                self.print_hand(self.dealer_hand, hide_dealer_card=True)
            dealer_total = self.calculate_hand(self.dealer_hand)
            if dealer_total > 21:
                print("Dealer busted! You win!")
            elif dealer_total > player_total:
                print("Dealer wins!")
            elif dealer_total < player_total:
                print("You win!")
            else:
                print("It's a tie!")

if __name__ == "__main__":
    game = Blackjack()
    game.play_game()
