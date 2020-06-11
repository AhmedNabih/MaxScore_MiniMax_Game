import pygame as pg
import numpy as np
import defaults as defu
import layout as lo
import movement as mov

from minimax import one_step_minimax, print_grid

def random_numbers():
    Result = {}
    for i in range(defu.GRID_X):
        for j in range(defu.GRID_Y):
            tempo = np.random.randint(low=-defu.R_NUM_RANGE, high=defu.R_NUM_RANGE+1)
            Result[str(i) + str(j)] = tempo

    return Result

def inits(name):
    pg.init()
    screen = pg.display.set_mode((defu.WINDOW_WIDTH, defu.WINDOW_HEIGHT))
    # Title
    pg.display.set_caption(name)

    return screen

if __name__ == '__main__':
    # input
    goalInt = int(input("Goal: "))
    maxMovesInt = int(input("Max Moves: "))

    # inits
    current_postion = [0, defu.GRID_Y-1]
    grid = random_numbers()
    print_grid(grid)
    mainScreen = inits("AI Puzzle Game")

    # default input
    totalMovesInt = 0
    scoreInt = 0

    WIN = False
    LOSS = False
    LOCK = True
    word = lo.make_string("", fontSize=20)
    MScore = lo.make_string("", fontSize=20)
    max_score = -defu.INFINTY
    # Game Loop
    running = True
    while running:
        # time delay
        #pg.time.delay(300)

        # main filter
        mainScreen.fill(defu.FO7LO2Y)

        # all events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if not defu.AI:
                # human player one move
                if event.type == pg.KEYDOWN:
                    pos = mov.movement_handler(event, current_postion)
                    rnad = np.random.randint(-defu.R_NUM_RANGE, defu.R_NUM_RANGE + 1)
                    oldVal = grid[str(current_postion[0]) + str(current_postion[1])]
                    grid[str(pos[0]) + str(pos[1])] += oldVal
                    new_score = grid[str(pos[0]) + str(pos[1])]
                    grid[str(current_postion[0]) + str(current_postion[1])] = rnad
                    current_postion = pos
                    scoreInt = grid[str(current_postion[0]) + str(current_postion[1])]
                    totalMovesInt += 1
                    max_score = max(max_score, scoreInt)
                    if scoreInt >= goalInt and LOCK:
                        word = lo.make_string("WIN", fontSize=20)
                        LOCK = False
                        # print win
                    if totalMovesInt == maxMovesInt:
                        if LOCK:
                            word = lo.make_string("LOSS", fontSize=20)
                        LOCK = False
                        WIN = True

        # draw text
        lo.draw_default_text(mainScreen)
        # draw dynamic grid
        rects = lo.draw_Grid(mainScreen)
        # highlight current postion
        lo.highlight_rectangle(mainScreen, rects, current_postion)
        # draw number for each rectangle
        lo.draw_numbers(mainScreen, rects, grid)

        if defu.AI:
            # MinMax algorithm
            # one AI step, update values
            if not WIN:
                scoreInt, current_postion = one_step_minimax(current_postion, grid, 3)
                totalMovesInt += 1
                max_score = max(max_score, scoreInt)
                if scoreInt >= goalInt and LOCK:
                    word = lo.make_string("WIN", fontSize=20)
                    LOCK = False
                    # print win
                if totalMovesInt == maxMovesInt:
                    if LOCK:
                        word = lo.make_string("LOSS", fontSize=20)
                    LOCK = False
                    WIN = True
                    # print loss

        # draw values
        lo.draw_values(mainScreen, goalInt, maxMovesInt, totalMovesInt, scoreInt)

        MScore = lo.make_string("With Max Score: " + str(max_score), fontSize=20)
        if not LOCK:
            marginLeft = -110
            lo.draw(mainScreen, word, (marginLeft+defu.WINDOW_WIDTH / 2.0 - 25, defu.WINDOW_HEIGHT-50))
            lo.draw(mainScreen, MScore, (marginLeft+defu.WINDOW_WIDTH / 2.0+42, defu.WINDOW_HEIGHT-50))

        # screen refresh or update
        pg.display.update()
