import copy
import random
import math

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

init = [[1,2,3],
        [4,0,6],
        [7,5,8]]

init2 = [[2,4,3],
        [1,0,6],
        [7,5,8]]

def heuristic(state, goal): #returns no of tiles misplaced, we try to minimize the score
    score = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                score += 1
    return score

def findZero(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

def getNeighbours(state):
    row, col = findZero(state)
    neighbours = []
    for direction in ['up', 'down', 'right', 'left']:
        if direction == 'up':
            tempstate = [row[:] for row in state]
            if row == 0:
                continue
            tempstate[row][col], tempstate[row-1][col] = tempstate[row-1][col], tempstate[row][col]
            neighbours.append((tempstate, 'up'))
        if direction == 'down':
            tempstate = [row[:] for row in state]
            if row == 2:
                continue
            tempstate[row][col], tempstate[row+1][col] = tempstate[row+1][col], tempstate[row][col]
            neighbours.append((tempstate, 'down'))
        if direction == 'right':
            tempstate = [row[:] for row in state]
            if col == 2:
                continue
            tempstate[row][col], tempstate[row][col+1] = tempstate[row][col+1], tempstate[row][col]
            neighbours.append((tempstate, 'right'))
        if direction == 'left':
            tempstate = [row[:] for row in state]
            if col == 0:
                continue
            tempstate[row][col], tempstate[row][col-1] = tempstate[row][col-1], tempstate[row][col]
            neighbours.append((tempstate, 'left'))
    return neighbours

def hillClimbing(init, goal):
    current = init
    path = []
    
    while True:
        curr_score = heuristic(current, goal)
        
        if curr_score == 0:
            print("Goal Reached!")
            return current

        neighbours = getNeighbours(current)
        best_state = None
        best_score = float('inf')
        best_move = None

        for neighbour_state, move in neighbours:
            score = heuristic(neighbour_state, goal)
            if score < best_score:
                best_score = score
                best_state = neighbour_state
                best_move = move

        # Check if we found a better "slope"
        if best_score >= curr_score:
            print("Stuck in Local Optimum (No better moves)")
            return current
        
        current = best_state
        print(f"Move: {best_move} | Heuristic: {best_score}")
        for row in current: print(row)

def simulatedAnnealing(init, goal, temp):
    current = init
    path = []
    
    while temp > 0.1:
        curr_score = heuristic(current, goal)
        
        if curr_score == 0:
            print("Goal Reached!")
            return curr_score, path

        neighbours = getNeighbours(current)
        
        neighbour, move = random.choice(neighbours)
        score = heuristic(neighbour, goal)
        if score < curr_score:
            current = neighbour
            print(f"Move: {move} | Heuristic: {score}")
            for row in current: print(row)
            path.append((current, move))
        else:
            epsilon = score-curr_score
            prob = math.exp(-epsilon/temp)
            if random.random() < prob:
                current = neighbour
                print(f"Taking bad move! Prob: {prob:.2f} | Temp: {temp:.2f}")
                print(f"Move: {move} | Heuristic: {score}")
                for row in current: print(row)
                path.append((current, move))
        temp = temp*0.99
    
    print("No Solution Found!!")
    return curr_score, path

def simulatedAnnealings(init, goal, temp):
    current = init
    path = []
    
    while temp > 0.1:
        curr_score = heuristic(current, goal)
        
        if curr_score == 0:
            return curr_score, path

        neighbours = getNeighbours(current)
        
        neighbour, move = random.choice(neighbours)
        score = heuristic(neighbour, goal)
        if score < curr_score:
            current = neighbour
            path.append((current, move))
        else:
            epsilon = score-curr_score
            prob = math.exp(-epsilon/temp)
            if random.random() < prob:
                current = neighbour
                path.append((current, move))
        temp = temp*0.99
    
    return curr_score, path

def randRestartAnnealing(init, goal, temp, n):
    paths = []
    best_path = None
    best_score = float('inf')
    for _ in range(n):
        score, path = simulatedAnnealings(init, goal, temp)
        paths.append((score, path))
    for score, path in paths:
        if score == best_score:
            if len(path) < len(best_path):
                best_score = score
                best_path = path
        elif score < best_score:
            best_score = score
            best_path = path

    print("Best Path Found is: ")
    for move in best_path: print(move)
    print(best_score)

#hillClimbing(init, goal)
#hillClimbing(init2, goal)
#print()
#print()
simulatedAnnealing(init2, goal, 10)
print()
print()
randRestartAnnealing(init2, goal, 10, 5)
