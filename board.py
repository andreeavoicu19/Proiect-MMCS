import turtle


pen = turtle.Turtle()
turtle.tracer(0)
pen.speed(1)
pen.color("white")
pen.hideturtle()


topLeft_x = -235
topLeft_y = 300


def text(message, x, y, size):
    font = ('Arial', size, 'normal')
    pen.penup()
    pen.goto(x, y)
    pen.write(message, align="left", font=font)


def drawGrid(board):
    dimCell = 50

    for row in range(0, 10):
        if (row % 3) == 0:
            pen.pensize(6)
        else:
            pen.pensize(1)
        pen.penup()
        pen.goto(topLeft_x, topLeft_y - row * dimCell)
        pen.pendown()
        pen.goto(topLeft_x + 9 * dimCell, topLeft_y - row * dimCell)

    for col in range(0, 10):
        if (col % 3) == 0:
            pen.pensize(6)
        else:
            pen.pensize(1)
        pen.penup()
        pen.goto(topLeft_x + col * dimCell, topLeft_y)
        pen.pendown()
        pen.goto(topLeft_x + col * dimCell, topLeft_y - 9 * dimCell)

    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] != 0:
                text(board[row][col], topLeft_x + col * dimCell + 9, topLeft_y - row * dimCell - dimCell + 8, 18)


