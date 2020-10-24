from graphics import graphics

class Button:

    def __init__(self, text, p1, p2):
        self.text = text

        self.rect = graphics.Rectangle(p1, p2)
        self.text = graphics.Text(self.rect.getCenter(), text)

        self.clicked = False
        self.visible = False

    def draw(self, window):
        self.rect.undraw()

        if self.visible:
            if self.clicked == True:
                self.rect.setFill("white")
            else:
                self.rect.setFill("grey")
            self.rect.draw(window)

            self.text.undraw()
            self.text.draw(window)
