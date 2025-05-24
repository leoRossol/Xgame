from game.Game import Game

if __name__ == "__main__":
    GRID_ROWS, GRID_COLS, CELL_SIZE = 10,15,40
    game = Game(GRID_ROWS, GRID_COLS, CELL_SIZE)
    game.run()