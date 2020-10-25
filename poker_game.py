import sys
from collections import defaultdict

values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

class poker:

    def __init__(self):

        self.card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                                "K": 13, "A": 14}

    ## returns the rank of each player

    def check_hand(self,hand):
        if self.check_royal_flush(hand):
            return 10
        if self.check_straight_flush(hand):
            return 9
        if self.check_four_of_a_kind(hand):
            return 8
        if self.check_full_house(hand):
            return 7
        if self.check_flush(hand):
            return 6
        if self.check_straight(hand):
            return 5
        if self.check_three_of_a_kind(hand):
            return 4
        if self.check_two_pairs(hand):
            return 3
        if self.check_one_pairs(hand):
            return 2
        return 1

    def check_royal_flush(self,hand):
        values = [i[0] for i in hand]
        value1 = ['J', '10', 'Q', 'K', 'A']
        if self.check_straight_flush(hand):
            if set(value1) == set(values):
                return True
            else:
                return False

    def check_straight_flush(self,hand):
        if self.check_flush(hand) and self.check_straight(hand):
            return True
        else:
            return False

    def check_four_of_a_kind(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1,4]:
            return True
        return False

    def check_full_house(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [2,3]:
            return True
        return False

    def check_flush(self,hand):
        suits = [i[1] for i in hand]
        if len(set(suits))==1:
            return True
        else:
            return False

    def check_straight(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v] += 1
        rank_values = [self.card_order_dict[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range==4):
            return True
        else:
            return False

    def check_three_of_a_kind(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if set(value_counts.values()) == set([3,1]):

            return True
        else:
            return False

    def check_two_pairs(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values())==[1,2,2]:
            return True
        else:
            return False

    def check_one_pairs(self,hand):

        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if 2 in value_counts.values():
            return True
        else:
            return False

    ##returns the highest card value if rank is 1
    def highest_card(self,hand):
        big = 0
        values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                  "A": 14}

        for i in hand:

            if values[i[0]] > big:
                big = values[i[0]]
        return (big)

    ##returns the highest value if ranks are same

    def find_value(self, hand):

        if self.check_one_pairs(hand) :
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda: 0)
            for v in values:
                value_counts[v] += 1
            inv_value_counts = {v: k for k, v in value_counts.items()}
            big = inv_value_counts[2]
            return(big)
        if self.check_three_of_a_kind(hand) :
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda: 0)
            for v in values:
                value_counts[v] += 1
            inv_value_counts = {v: k for k, v in value_counts.items()}
            big = inv_value_counts[3]
            return (big)

        if self.check_four_of_a_kind(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda: 0)
            for v in values:
                value_counts[v] += 1
            inv_value_counts = {v: k for k, v in value_counts.items()}

            big = inv_value_counts[4]
            return (big)
        if self.check_two_pairs(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda: 0)
            for v in values:
                value_counts[v] += 1
            inv_value_counts = {v: k for k, v in value_counts.items()}

            big = inv_value_counts[1]
            return (big)

        if self.check_straight_flush(hand):
            big = 0
            values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                      "K": 13,
                      "A": 14}
            for i in hand:

                if values[i[0]] > big:
                    big = values[i[0]]
            return (big)
        if self.check_flush(hand):
            big = 0
            values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                      "K": 13,
                      "A": 14}
            for i in hand:

                if values[i[0]] > big:
                    big = values[i[0]]
            return (big)
        if self.check_straight(hand):
            big = 0
            values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                      "K": 13,
                      "A": 14}
            for i in hand:

                if values[i[0]] > big:
                    big = values[i[0]]
            return (big)
        if self.check_full_house(hand):
            values = [i[0] for i in hand]
            value_counts = defaultdict(lambda: 0)
            for v in values:
                value_counts[v] += 1
            inv_value_counts = {v: k for k, v in value_counts.items()}
            big = inv_value_counts[3]
            return (big)


## main

sys.stdin=open("poker-hands.txt")
P1W=0
P2W=0
Player = poker()
for line in sys.stdin:
    cards= line

    cards = list(map(lambda x:x, cards.split()))
    hand = cards[:5]
    deck = cards[5:]


    P1= Player.check_hand(hand)
    P2= Player.check_hand(deck)

    ## comparing the ranks of Player 1 and Player 2

    if P1 > P2:
        P1W += 1
    elif P1 < P2:
        P2W += 1
    elif P1 == P2 == 1:
        if Player.highest_card(hand)> Player.highest_card(deck):
            P1W+=1
        else:
            P2W+=1
    elif (P1 == P2) :
        if values[Player.find_value(hand)] > values[Player.find_value(deck)]:
            P1W+=1
        else:
            P2W+=1


print("Output of provided test file")
print("Player 1:",P1W,"\nPlayer 2:", P2W)
