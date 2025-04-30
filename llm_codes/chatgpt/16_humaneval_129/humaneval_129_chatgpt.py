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
