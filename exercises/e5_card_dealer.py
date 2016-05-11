from random import shuffle


class Card(object):
    def __init__(self, tuple_number_color):
        self._id = tuple_number_color

    def __str__(self):
        return "|" + str(self._id[0]) + " " + str(self._id[1]) + "|"


class Deck(object):
    def __init__(self):
        self._cards = []
        self.numbers = ['2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ', 'A ']
        self.colors = ['c', 'd', 'h', 's']
        for number in self.numbers:
            for color in self.colors:
                self._cards.append(Card((number, color)))

    def insert(self, card):
        if card:
            if not card in self._cards:
                self._cards.insert(0, card)

    def pop(self):
        return self._cards.pop()

    def shuffle(self):
        shuffle(self._cards)

    def sort(self):
        self._cards = sorted(self._cards)


class Player(object):
    def __init__(self, name):
        self.name = name
        self._first_card = None
        self._second_card = None

    def receive_cards(self, first_card=None, second_card=None):
        if first_card:
            self._first_card = first_card
        if second_card:
            self._second_card = second_card

    def return_cards(self):
        temp_list = [self._first_card, self._second_card]
        self._first_card = None
        self._second_card = None
        return temp_list

    def show(self):
        print self.name + " ",
        print str(self._first_card) + " " + str(self._second_card)


class Table(object):
    def __init__(self):
        # _card_slots = [flop1, flop2, flop3, turn, river]
        self._card_slots = [None, None, None, None, None]

    def receive_cards(self, flop1=None, flop2=None, flop3=None, turn=None, river=None):
        if flop1: self._card_slots[0] = flop1
        if flop2: self._card_slots[1] = flop2
        if flop3: self._card_slots[2] = flop3
        if turn: self._card_slots[3] = turn
        if river: self._card_slots[4] = river

    def return_cards(self):
        temp_cards = self._card_slots
        self._card_slots = [None, None, None, None, None]
        return temp_cards

    def show(self):
        for slot in self._card_slots:
            if slot:
                print slot,
            else:
                print "|    |",
        print


class Dealer(object):
    def __init__(self, table, players):
        self._table = table
        self._players = players

        self._deck = Deck()

    def shuffle_cards(self):
        print "shuffling..."
        self._deck.shuffle()

    def deal_players(self):
        print "dealing players..."
        for player in self._players:
            self._burn_card()
            player.receive_cards(self._deck.pop(), self._deck.pop())

    def deal_flop(self):
        print "dealing flop..."
        self._burn_card()
        self._table.receive_cards(flop1 = self._deck.pop(),
                                  flop2 = self._deck.pop(),
                                  flop3 = self._deck.pop())

    def deal_turn(self):
        print "dealing turn..."
        self._burn_card()
        self._table.receive_cards(turn = self._deck.pop())

    def deal_river(self):
        print "dealing river..."
        self._burn_card()
        self._table.receive_cards(river = self._deck.pop())

    def collect_cards(self):
        print "collecting cards..."
        for player in self._players:
            cards = player.return_cards()
            for card in cards:
                self._deck.insert(card)
        table_cards = self._table.return_cards()
        for card in table_cards:
            self._deck.insert(card)

    def _burn_card(self):
        self._deck.insert(self._deck.pop())

    def show_deck(self):
        print "Showing deck..."
        print "count: " + str(len(self._deck._cards))
        for card in self._deck._cards:
            print card


class Game(object):
    def __init__(self, players):
        self._players = players
        self._table = Table()
        self._dealer = Dealer(self._table, self._players)

    def show_table(self):
        self._table.show()

    def show_players(self):
        for player in self._players:
            player.show()
            print

    def play(self):
        self._dealer.show_deck()
        raw_input()
        self._dealer.shuffle_cards()
        self._dealer.show_deck()
        raw_input()
        self._dealer.deal_players()
        self.show_players()
        self._dealer.deal_flop()
        self.show_table()
        raw_input()
        self._dealer.deal_turn()
        self.show_table()
        raw_input()
        self._dealer.deal_river()
        self.show_table()
        raw_input()
        self._dealer.show_deck()
        raw_input()
        self._dealer.collect_cards()
        self._dealer.show_deck()


def play_texas_holdem():
    texas = Game([Player('Gimi'), Player('Paul'), Player('Luci')])
    texas.play()

if __name__ == "__main__":
    play_texas_holdem()
