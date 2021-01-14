from board import *
from time import sleep

backtracks = 0


def checkGrid(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                return False

    return True


def solveGrid(board, backtracks):
    moves = 0
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if board[row][col] == 0:
            for value in range(0, 10):
                if not (value in board[row]):
                    if not value in (
                            board[0][col], board[1][col], board[2][col], board[3][col], board[4][col], board[5][col],
                            board[6][col], board[7][col], board[8][col]):
                        if row < 3:
                            if col < 3:
                                box = [board[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                box = [board[i][3:6] for i in range(0, 3)]
                            else:
                                box = [board[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                box = [board[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                box = [board[i][3:6] for i in range(3, 6)]
                            else:
                                box = [board[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                box = [board[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                box = [board[i][3:6] for i in range(6, 9)]
                            else:
                                box = [board[i][6:9] for i in range(6, 9)]

                        if not value in (box[0] + box[1] + box[2]):
                            board[row][col] = value
                            moves += 1
                            print("Numar de completari in randul", row + 1, "- coloana ", col + 1, " : ", moves)
                            pen.clear()
                            drawGrid(board)
                            pen.getscreen().update()
                            backtracks += 1
                            if checkGrid(board):
                                print("Gridul este complet si verificat.")
                                print("Numarul de backtrack-uri realizate: ", backtracks)
                                print("\n")
                                return True
                            else:
                                if solveGrid(board, backtracks):
                                    return True
            break
    board[row][col] = 0
