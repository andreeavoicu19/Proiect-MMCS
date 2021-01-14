from turtle import Screen
from self_solver import *
from sudoku import Sudoku
from time import sleep
import time



def main():
    height = 600
    width = 600
    screen = Screen()
    screen.screensize(width, height)
    screen.title("Simulare Sudoku")
    screen.bgcolor("#1a0000")

    print("  __________________________________________  ")
    print(" |  Simularea unui joc de Sudoku pe nivele  | ")
    print(" |__________________________________________| \n")

    i = int(input("Alegeti nivelul de dificultate: \n 1 = Easy ; 2 = Medium ; 3 - Hard \n"))

    if i == 1:
        # Easy
        puzzle = Sudoku(3).difficulty(0.2)
        print(puzzle)
        board = puzzle.returnBoard()
        for i in range(9):
            for j in range(9):
                if board[i][j] is None:
                    board[i][j] = 0

    elif i == 2:
        # Medium
        puzzle = Sudoku(3).difficulty(0.5)
        print(puzzle)
        board = puzzle.returnBoard()
        for i in range(9):
            for j in range(9):
                if board[i][j] is None:
                    board[i][j] = 0
    else:
        # Hard
        puzzle = Sudoku(3).difficulty(0.6)
        print(puzzle)
        board = puzzle.returnBoard()
        for i in range(9):
            for j in range(9):
                if board[i][j] is None:
                    board[i][j] = 0

    drawGrid(board)
    pen.getscreen().update()
    sleep(3)
    start = time.time()

    solved = solveGrid(board, backtracks)

    if solved:
        print("| Sfarsit joc |")
        text(" Sfarsit joc ", -70, -230, 20)
    else:
        print("Nu poate rezolva gridul.")
        text("Nu poate rezolva gridul.", -130, -230, 20)

    end = time.time()
    print("Timpul de joc :", round(end - start), "secunde")
    sleep(7)
    pen.getscreen().update()


main()
