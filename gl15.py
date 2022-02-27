from random import shuffle

class Card:
    suits = ["пика",
             "червей",
             "бубей",
             "треф"]

    values = [None, None, '2', '3',
              '4', '5', '6', '7',
              '8', '9', '10',
              'валет', 'дама',
              'король', 'туз']

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        '''настройка, с помощью которой программа понимает, в каких случаях карта будет меньше другой'''
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
        else:
            return False
        return False

    def __gt__(self, c2):
        '''то же самое только с ситуацией, когда карта должна быть больше другой'''
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
        else:
            return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' ' + self.suits[self.suit]
        return v


class Deck:
    cards = []

    def __init__(self):
        for i in range(2, 14):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('имя игрока 1: ')
        name2 = input('имя игрока 2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = '{} забирает карты'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} кладет {}, а {} кладет {}'
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Начинаем!')
        while len(cards) >= 2:
            msg = 'Введите X для выхода. Введите любой другой символ для начала игры'
            response = input(msg)
            if response == 'X':
                break
            p1c = self.deck.rm_cards()
            p2c = self.deck.rm_cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c >p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print('Игра окончена. {} выиграл!'.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p1.name
        return 'Ничья!'

game = Game()
game.play_game()
