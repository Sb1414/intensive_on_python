from collections import Counter
import random

class Player: # базовый класс для различных типов игроков
    def __init__(self):
        self.score = 0 # счет игрока

    def play(self, other_player): # метод заполнитель, будет переопределен в подклассах
        pass

class Cheater(Player): # подкласс Player
    def play(self, other_player):
        # счет игрока увеличивается на 3, а счет другого игрока уменьшается на 1
        self.score += 3
        other_player.score -= 1

class Cooperator(Player): # подкласс Player
    def play(self, other_player):
        # счет игрока увеличивается на 2, а счет другого игрока тоже увеличивается на 2
        self.score += 2
        other_player.score += 2

class Imitator(Player):
    def __init__(self):
        super().__init__()
        self.last_action = None

    def play(self, other_player):
        # повторяет действие последнего сыгранного игрока
        # Если это первый ход, счет игрока и другого игрока увеличиваются на 2, и последним действием становится Cooperator()
        if self.last_action:
            self.last_action.play(other_player)
        else:
            self.score += 2
            other_player.score += 2
            self.last_action = Cooperator()

class Grudger(Player):
    def __init__(self):
        super().__init__()
        # флаг cooperated, который изначально установлен в True.
        self.cooperated = True

    def play(self, other_player):
        # сотрудничает, увеличивая счет игрока и другого игрока на 2
        if self.cooperated:
            self.score += 2
            other_player.score += 2
        else:
            # если флаг cooperated равен False, счет другого игрока увеличивается на 3
            other_player.score += 3

    def update(self, other_player):
        # обновляет флаг cooperated на основе счета другого игрока
        if other_player.score == 3:
            self.cooperated = False

class Detective(Player):
    def __init__(self):
        super().__init__()
        # список actions, изначально содержащий четыре действия: Cooperator(), Cheater(), Cooperator(), Cooperator()
        self.actions = [Cooperator(), Cheater(), Cooperator(), Cooperator()]

    def play(self, other_player):
        # выбирает первое действие из списка, выполняет его на другом игроке, а затем перемещает это действие в конец списка
        action = self.actions.pop(0)
        action.play(other_player)
        self.actions.append(action)

    def update(self, other_player):
        # обновляет список actions на основе счета другого игрока
        if other_player.score == 3:
            self.actions = [Imitator()] * 4

class Game:
    def __init__(self, matches=10):
        # В конструкторе он принимает необязательный аргумент matches, который устанавливает количество матчей по умолчанию в 10
        self.matches = matches
        # атрибут registry, который использует объект Counter для отслеживания счета различных типов игроков
        self.registry = Counter()

    def play(self, player1, player2): #запускает серию матчей между двумя игроками
        # В каждом матче вызывается метод play для каждого игрока, а затем обновляется счет в registry
        # на основе типа игрока и его счета. Если игрок является экземпляром Grudger,
        # вызывается метод update для обновления флага cooperated.
        # Если игрок является экземпляром Detective, вызывается метод update для обновления списка actions.
        for _ in range(self.matches):
            player1.play(player2)
            player2.play(player1)
        self.registry[player1.__class__.__name__] += player1.score
        self.registry[player2.__class__.__name__] += player2.score
        if isinstance(player1, Grudger):
            player1.update(player2)
        if isinstance(player2, Grudger):
            player2.update(player1)
        if isinstance(player1, Detective):
            player1.update(player2)
        if isinstance(player2, Detective):
            player2.update(player1)

    def top3(self):
        # выводит три наиболее высоких счета игроков из registry.
        top_scores = self.registry.most_common(3)
        for player, score in top_scores:
            print(player, score)

# Simulating the game
game = Game()

player1 = Cheater()
player2 = Cooperator()
game.play(player1, player2)

player1 = Cooperator()
player2 = Imitator()
game.play(player1, player2)

player1 = Grudger()
player2 = Detective()
game.play(player1, player2)

game.top3()
