############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   DeepSeek-V3
#
# prompt: 
#   "\ndef minPath(grid, k):\n    \"\"\"\n    Given a grid with N rows and N columns (N >= 2) and a positive integer k, \n    each cell of the grid contains a value. Every integer in the range [1, N * N]\n    inclusive appears exactly once on the cells of the grid.\n\n    You have to find the minimum path of length k in the grid. You can start\n    from any cell, and in each step you can move to any of the neighbor cells,\n    in other words, you can go to cells which share an edge with you current\n    cell.\n    Please note that a path of length k means visiting exactly k cells (not\n    necessarily distinct).\n    You CANNOT go off the grid.\n    A path A (of length k) is considered less than a path B (of length k) if\n    after making the ordered lists of the values on the cells that A and B go\n    through (let's call them lst_A and lst_B), lst_A is lexicographically less\n    than lst_B, in other words, there exist an integer index i (1 <= i <= k)\n    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have\n    lst_A[j] = lst_B[j].\n    It is guaranteed that the answer is unique.\n    Return an ordered list of the values on the cells that the minimum path go through.\n\n    Examples:\n\n        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3\n        Output: [1, 2, 1]\n\n        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1\n        Output: [1]\n    \"\"\"\n"
#
# response:
#
def minPath(grid, k):
    N = len(grid)
    # Find the position of the minimum value in the grid
    min_val = float('inf')
    start_i, start_j = -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                start_i, start_j = i, j
    
    path = [min_val]
    current_i, current_j = start_i, start_j
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for _ in range(k - 1):
        # Explore all adjacent cells to find the smallest value
        next_val = float('inf')
        next_i, next_j = -1, -1
        for di, dj in directions:
            ni, nj = current_i + di, current_j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if grid[ni][nj] < next_val:
                    next_val = grid[ni][nj]
                    next_i, next_j = ni, nj
        # Move to the smallest adjacent cell
        path.append(next_val)
        current_i, current_j = next_i, next_j
    
    return path
