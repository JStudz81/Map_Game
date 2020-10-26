from time import sleep

from battle import Battle
from map import Map
from menu import Menu
from messageBoard import MessageBoard
from nation import Nation
from graphics import graphics
from shapely import geometry
import random
import json
from ShapeToGraphics import Shape
from region import Region


class Game:

    def __init__(self):

        self.map = Map()
        self.menu = Menu(self.map.window)
        self.messageBoard = MessageBoard(self.map.window,graphics.Point(300, 400), graphics.Point(500, 500))
        self.turn_indicator = MessageBoard(self.map.window, graphics.Point(200, 450), graphics.Point(300, 500))
        self.event_box = MessageBoard(self.map.window, graphics.Point(300, 0), graphics.Point(500, 100))

        self.nations = []
        self.regions = []

        self.load_nations()

        self.map.regions = self.regions
        self.selectedNation = None

        self.player_nation = self.nations[0]
        self.player_turn = True

        print(self.nations[0])

    def load_nations(self):
        f = open("map_maker/nation_geometry.txt")

        rows = f.readlines()

        for row in rows:
            tempNation = json.loads(row)
            points = []
            for i in tempNation['points']:
                points.append(geometry.Point(tempNation['points'][i]['x'],tempNation['points'][i]['y']))
            nation = Nation(tempNation['name'], tempNation['color'], 1000)
            region = Region(points)
            region.shape.color = nation.color
            region.name = nation.name
            nation.regions = [region]
            self.nations.append(nation)
            self.regions.append(region)

    def draw(self):
        self.map.draw()
        self.menu.draw()
        self.messageBoard.draw()
        self.turn_indicator.draw()

    def run(self):
        playing = True
        while playing:
            self.draw()
            self.player_turn_action()
            self.draw()
            self.random_event(self.player_nation)

            for nation in self.nations:
                if nation != self.player_nation and nation.soldiers != 0:
                    self.ai_turn(nation)

            first = None
            playing = False
            for nation in self.nations:
                if nation.soldiers > 0 and first is None:
                    first = nation
                elif nation.soldiers > 0:
                    playing = True

            if self.player_nation.soldiers == 0:
                playing = False

            self.player_turn = True

    def player_turn_action(self):
        attack_move = True
        recruit_move = True
        self.menu.attackButton.visible = True
        self.menu.recruitButton.visible = True

        while self.player_turn:
            self.turn_indicator.new_message(self.player_nation.name)
            self.turn_indicator.change_color(self.player_nation.color)
            clickedPoint = self.map.window.getMouse()

            clicked = self.what_was_clicked(clickedPoint)

            if clicked is None:
                self.draw()
            elif clicked[0] == 'nation' and self.selectedNation != clicked[1]:
                self.selectedNation = clicked[1]
                self.menu.loadNation(clicked[1], self.selectedNation == self.player_nation)
            elif clicked[0] == 'attack' and self.selectedNation == self.player_nation:
                self.menu.attackButton.clicked = True
                self.menu.draw()
                attackingClick = self.map.window.getMouse()

                defender = self.what_was_clicked(attackingClick)
                if defender is not None and defender[0] == 'nation' and defender[1] != self.selectedNation:
                    result = self.battle(defender[1], self.selectedNation)

                    self.messageBoard.new_message(result)
                    attack_move = False
                    self.menu.attackButton.visible = False
                    self.menu.draw()

                self.menu.attackButton.clicked = False
            elif clicked[0] == 'recruit' and self.selectedNation == self.player_nation:
                clicked[1].clicked = True
                self.menu.draw()
                self.recruit(self.selectedNation, int(self.menu.recruit_amount.getText()))
                clicked[1].clicked = False
                recruit_move = False
                self.menu.recruitButton.visible = False
                self.menu.draw()

            self.player_turn = recruit_move or attack_move


    def ai_turn(self, nation):
        self.turn_indicator.new_message(nation.name)
        self.turn_indicator.change_color(nation.color)
        target = None
        while target is None:
            target = self.nations[random.randint(0, len(self.nations) - 1)]
            if target == nation or target.soldiers == 0:
                target = None
        self.recruit(nation, random.randint(0, int(nation.money * 10)))
        sleep(1)
        self.messageBoard.new_message(self.battle(target, nation))

        self.random_event(nation)
        self.draw()

    def random_event(self, nation):
        sleep(1)
        event = self.events(random.randint(1,3))
        event(nation, self.event_box)
        self.draw()
        self.map.window.getMouse()
        self.event_box.undraw()


    def events(self, index):
        switcher = {
            1: self.soldierEvent,
            2: self.moneyEvent,
            3: self.loseEvent
        }
        return switcher.get(index)

    def soldierEvent(self, nation, event_box: MessageBoard):
        nation.soldiers = nation.soldiers + 500
        event_box.new_message(nation.name + " gained 500 soldiers!")

    def moneyEvent(self, nation, event_box: MessageBoard):
        nation.money = nation.money + 100
        event_box.new_message(nation.name + " gained 100 gp!")

    def loseEvent(self, nation, event_box: MessageBoard):
        print("you lose")
        event_box.new_message("That fucking sucks.")

    def what_was_clicked(self, point: graphics.Point):
        if 0 < point.getX() < 50 and 400 < point.getY() < 425:
            return 'attack', self.menu.attackButton

        if self.menu.recruitButton.rect.getP1().getX() < point.getX() < self.menu.recruitButton.rect.getP2().getX() and self.menu.recruitButton.rect.getP1().getY() < point.getY() < self.menu.recruitButton.rect.getP2().getY():
            return 'recruit', self.menu.recruitButton

        for nation in self.nations:
            for region in nation.regions:
                if region.shape.polygon.contains(geometry.Point(point.x, point.y)):
                    return 'nation', nation

    def recruit(self, nation: Nation, amount):
        if amount / 10 <= nation.money:
            nation.soldiers = nation.soldiers + amount
            nation.money = nation.money - (amount/10)
            self.messageBoard.new_message(nation.name + " has recruited " + str(amount) + " Soldiers")
        else:
            self.messageBoard.new_message("Not Enough Money!")
        self.draw()

    def battle(self, defender: Nation, attacker: Nation):
        battleInfo = ""

        battleInfo = battleInfo + attacker.name + " has attacked " + defender.name + "!\n"

        battle = Battle(attacker, defender)

        battleInfo = battleInfo + defender.name + " lost " + str(battle.outcome[1]) + " soldiers\n"
        battleInfo = battleInfo + attacker.name + " lost " + str(battle.outcome[0]) + " soldiers\n"

        return battleInfo



if __name__ == '__main__':
    game = Game()
    game.run()