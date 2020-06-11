import pygame as pg
import defaults as defu

def movement_handler(event, current_postion):
    if event.key == pg.K_UP:
        current_postion = move(current_postion, up=True)
    elif event.key == pg.K_DOWN:
        current_postion = move(current_postion, down=True)
    elif event.key == pg.K_LEFT:
        current_postion = move(current_postion, left=True)
    elif event.key == pg.K_RIGHT:
        current_postion = move(current_postion, right=True)
    return current_postion

def safe_state(X, Y):
    if X < 0 or X > defu.GRID_X - 1:
        return False
    elif Y < 0 or Y > defu.GRID_Y - 1:
        return False

    return True

# up Y--, down Y++, left X--, right X++
def move(postion, up=False ,down=False ,left=False ,right=False):
    X = postion[0]
    Y = postion[1]
    defValue = 1

    if left:
        X = X - defValue
    elif right:
        X = X + defValue
    elif up:
        Y = Y - defValue
    elif down:
        Y = Y + defValue

    if safe_state(X, Y):
        postion = [X, Y]

    return postion