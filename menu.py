from button import Button
from graphics import graphics


class Menu:

    def __init__(self, window: graphics.GraphWin):
        self.nation = None
        self.window = window

        position1 = graphics.Point(0, 400)
        position2 = graphics.Point(200, 500)

        self.rect = graphics.Rectangle(position1, position2)
        self.rect.setOutline("black")
        self.rect.setFill("grey")

        self.text = None

        self.attackButton = Button('Attack', graphics.Point(0, 400), graphics.Point(50, 425))
        self.recruitButton = Button('Recruit', graphics.Point(50,400), graphics.Point(100, 425))
        self.recruit_amount = graphics.Entry(graphics.Point(125, 412.5), 4)

    def loadNation(self, nation, player: bool):
        self.nation = nation
        self.attackButton.visible = player
        self.recruitButton.visible = player
        self.recruit_amount.undraw()
        self.text = graphics.Text(self.rect.getCenter(),
                                  self.nation.name + " - Money: " + str(self.nation.money) + " - Soldiers: " + str(
                                      self.nation.soldiers))
        self.draw()

    def draw(self):
        self.rect.undraw()
        self.rect.draw(self.window)

        if self.text is not None:
            self.text.setText(self.nation.name + " - Money: " + str(self.nation.money) + " - Soldiers: " + str(self.nation.soldiers))
            self.text.undraw()
            self.text.draw(self.window)

        self.attackButton.draw(self.window)
        self.recruitButton.draw(self.window)

        if self.attackButton.visible:
            self.recruit_amount.undraw()
            self.recruit_amount.draw(self.window)