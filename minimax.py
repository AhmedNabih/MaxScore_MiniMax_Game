import defaults as defu
import movement as mov
import numpy as np
import copy

def get_children_max(postion):
    X = postion[0]
    Y = postion[1]
    # up Y--, down Y++, left X--, right X++
    up = [X, Y-1]
    down = [X, Y+1]
    left = [X-1, Y]
    right = [X+1, Y]
    children_temp = [up, down, left, right]
    children = []
    for child in children_temp:
        if mov.safe_state(child[0], child[1]):
            children.append(child)

    return children

def get_children_min():
    listaya = []
    for i in range(-defu.R_NUM_RANGE, defu.R_NUM_RANGE+1):
        listaya.append(i)

    return listaya

def catch_flag(postion, grid):
    X = postion[0]
    Y = postion[1]
    # up Y--, down Y++, left X--, right X++
    up = [X, Y - 1]
    down = [X, Y + 1]
    left = [X - 1, Y]
    right = [X + 1, Y]
    children_temp = [up, down, left, right]
    for child in children_temp:
        if mov.safe_state(child[0],child[1]) and grid[str(child[0])+str(child[1])] == defu.FLAG:
            return child[0], child[1]
    return None, None

def print_grid(grid):
    print(str(grid['00']) + " " + str(grid['10']) + " " + str(grid['20']))
    print(str(grid['01']) + " " + str(grid['11']) + " " + str(grid['21']))
    print(str(grid['02']) + " " + str(grid['12']) + " " + str(grid['22']))

def minimax(postion, gridy, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        return gridy[str(postion[0])+str(postion[1])], None

    if maximizingPlayer:
        maxEval = -defu.INFINTY
        children = get_children_max(postion)
        retPos = None
        for child in children:
            grid = copy.deepcopy(gridy)
            val1 = grid[str(child[0])+str(child[1])]
            val2 = grid[str(postion[0])+str(postion[1])]
            grid[str(child[0])+str(child[1])] = val1 + val2
            grid[str(postion[0]) + str(postion[1])] = defu.FLAG

            eval, _ = minimax(child, grid, depth-1, alpha, beta, False)
            if eval > maxEval:
                retPos = child
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return maxEval, retPos

    else:
        minEval = defu.INFINTY
        children = get_children_min()
        for child in children:
            grid = copy.deepcopy(gridy)
            xFlag, yFlag = catch_flag(postion, grid)
            if xFlag is None:
                break
            grid[str(xFlag)+str(yFlag)] = child

            eval, _ = minimax(postion, grid, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return minEval, None

def one_step_minimax(postion, grid, depth):
    alpha = -defu.INFINTY
    beta = defu.INFINTY
    result, pos = minimax(postion, grid, depth, alpha, beta, True)

    rnad = np.random.randint(-defu.R_NUM_RANGE, defu.R_NUM_RANGE+1)
    oldVal = grid[str(postion[0]) + str(postion[1])]
    grid[str(pos[0]) + str(pos[1])] += oldVal
    new_score = grid[str(pos[0]) + str(pos[1])]
    grid[str(postion[0]) + str(postion[1])] = rnad

    return new_score, pos


"""
if __name__ == '__main__':
    postion = [0, GRID_Y-1]
    #grid = {"00":1, "01":1, "02":0, "10":-1, "11":0, "12":1, "20":0, "21":1, "22":-1}

    #grid = {"00":1, "01":0, "02":-1, "10":-1, "11":0, "12":5, "20":0, "21":1, "22":-1}
    #postion = [1, 2]
    #depth = 5
    #goal = 10

    #grid = random_numbers()
    grid = {"00": -1, "01": 1, "02": 1, "10": -1, "11": 1, "12": -1, "20": 1, "21": -1, "22": 1}
    print_grid(grid)
    print("###################")
    depth = 5
    goal = 75
    score = 0

    #allPos = [[]]

    #np.random.seed(5)
    for i in range(10000):
        alpha = -INFINTY
        beta = INFINTY
        print_grid(grid)
        result, pos = minimax(postion, grid, depth, alpha, beta, True, goal, score)

        rnad = np.random.randint(-1, 2)
        oldVal = grid[str(postion[0])+str(postion[1])]
        grid[str(pos[0])+str(pos[1])] += oldVal
        score = grid[str(pos[0])+str(pos[1])]
        grid[str(postion[0]) + str(postion[1])] = rnad

        postion = pos
        print(score, pos)
        print("")

        if score >= goal:
            print(i)
            break
            """