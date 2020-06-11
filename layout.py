import pygame as pg
import defaults as defu

marginX = 40

def make_string(word, fontName='Comic Sans MS', fontSize=30):
    font = pg.font.SysFont(fontName, fontSize, 30)
    word = str(word)
    resultWord = font.render(word, True, (0,0,0))
    return resultWord

def init_text():
    goalText = make_string("Goal:")
    scoreText = make_string("Score:")
    maxMovesText = make_string("Max Moves:")
    totalMovesText = make_string("Total Moves:")

    defaultStrings = {"goal": goalText, "score": scoreText, "maxMoves": maxMovesText, "totalMoves": totalMovesText}

    return defaultStrings

def highlight_rectangle(screen, rects, current_postion):
    rectX = current_postion[0]
    rectY = current_postion[1]
    rect = rects["rect" + str(rectX) + str(rectY)]
    screen.fill(defu.LIGHTORANGE, rect)

def draw(screen, content, coord):
    screen.blit(content, coord)

def draw_values(screen, goalInt, maxMovesInt, totalMovesInt, scoreInt):
    sz = 30
    goalString = make_string(goalInt, fontSize=sz)
    scoreString = make_string(scoreInt, fontSize=sz)
    maxMovesString = make_string(maxMovesInt, fontSize=sz)
    totalMovesString = make_string(totalMovesInt, fontSize=sz)

    draw(screen, maxMovesString, (235+marginX, 0))
    draw(screen, totalMovesString, (235+marginX, 40))
    draw(screen, goalString, (615+marginX, 0))
    draw(screen, scoreString, (615+marginX, 40))

def draw_default_text(screen):
    defaultText = init_text()
    draw(screen, defaultText["maxMoves"], (35+marginX, 0))
    draw(screen, defaultText["totalMoves"], (15+marginX, 40))
    draw(screen, defaultText["goal"], (525+marginX, 0))
    draw(screen, defaultText["score"], (500+marginX, 40))

def draw_Grid(screen):
    blockSizeX = 230
    blockSizeY = 140
    rects = {}
    for x in range(defu.GRID_X):
        for y in range(defu.GRID_Y):
            rect = pg.Rect(x*blockSizeX, y*blockSizeY,blockSizeX, blockSizeY)
            rect = pg.Rect.move(rect, 55, 120)
            screen.fill(defu.LIGHTBLUE, rect)
            pg.draw.rect(screen, defu.WHITE, rect, 1)
            rects["rect" + str(x) + str(y)] = rect

    return rects

def draw_numbers(screen, rects, numbers):
    for x in range(defu.GRID_X):
        for y in range(defu.GRID_Y):
            rect = rects["rect" + str(x) + str(y)]
            rect_center = rect.center
            number = numbers[str(x)+str(y)]
            temp = make_string(number, fontSize=20)
            w = temp.get_width() / 2.0
            h = temp.get_height() / 2.0
            draw(screen, temp, (rect_center[0] - w, rect_center[1] - h))