############################
# @Authors
# Student Name: Erblina Nivokazi
# Student ID: 150200917
############################

# used LLM model: 
#   GPT-4o
#
# prompt: 
#   "\ndef minPath(grid, k):\n    \"\"\"\n    Given a grid with N rows and N columns (N >= 2) and a positive integer k, \n    each cell of the grid contains a value. Every integer in the range [1, N * N]\n    inclusive appears exactly once on the cells of the grid.\n\n    You have to find the minimum path of length k in the grid. You can start\n    from any cell, and in each step you can move to any of the neighbor cells,\n    in other words, you can go to cells which share an edge with you current\n    cell.\n    Please note that a path of length k means visiting exactly k cells (not\n    necessarily distinct).\n    You CANNOT go off the grid.\n    A path A (of length k) is considered less than a path B (of length k) if\n    after making the ordered lists of the values on the cells that A and B go\n    through (let's call them lst_A and lst_B), lst_A is lexicographically less\n    than lst_B, in other words, there exist an integer index i (1 <= i <= k)\n    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have\n    lst_A[j] = lst_B[j].\n    It is guaranteed that the answer is unique.\n    Return an ordered list of the values on the cells that the minimum path go through.\n\n    Examples:\n\n        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3\n        Output: [1, 2, 1]\n\n        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1\n        Output: [1]\n    \"\"\"\n"
#
# response:
#
import heapq

def minPath(grid, k):
    n = len(grid)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    heap = []

    # Initialize heap with all cells
    for i in range(n):
        for j in range(n):
            heapq.heappush(heap, ([grid[i][j]], i, j))

    while heap:
        path, x, y = heapq.heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                new_path = path + [grid[nx][ny]]
                heapq.heappush(heap, (new_path, nx, ny))
