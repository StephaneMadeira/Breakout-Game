from turtle import Turtle

COLORS = ["orange", "yellow", "green"]


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.total_blocks = []
        self.x = 550

    def create_blocks(self):
        new_block = Turtle(shape="square")

        if len(self.total_blocks) < 10:
            new_block.color(COLORS[0])
            new_block.penup()
            new_block.shapesize(stretch_wid=2, stretch_len=6)
            new_block.goto(self.x, 300)
            self.total_blocks.append(new_block)
            self.x -= 123

        elif 9 < len(self.total_blocks) < 21:
            new_block.color(COLORS[1])
            new_block.penup()
            new_block.shapesize(stretch_wid=2, stretch_len=6)
            new_block.goto(self.x+50, 250)
            self.total_blocks.append(new_block)
            self.x += 123

        elif 20 < len(self.total_blocks) < 32:
            new_block.color(COLORS[2])
            new_block.penup()
            new_block.shapesize(stretch_wid=2, stretch_len=6)
            new_block.goto(self.x-50, 200)
            self.total_blocks.append(new_block)
            self.x -= 123
        else:
            pass