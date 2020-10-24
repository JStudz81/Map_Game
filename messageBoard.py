from graphics import graphics

class MessageBoard:

    def __init__(self, window, p1, p2):

        self.window = window

        position1 = p1
        position2 = p2

        self.rect = graphics.Rectangle(position1, position2)
        self.rect.setOutline("black")
        self.rect.setFill("grey")

        self.text = None

    def change_color(self, color):
        self.rect.setFill(color)

    def draw(self):
        self.rect.undraw()
        self.rect.draw(self.window)

        if self.text is not None:
            self.text.undraw()
            self.text.draw(self.window)

    def new_message(self, text):
        self.text = graphics.Text(self.rect.getCenter(), text)
        self.draw()