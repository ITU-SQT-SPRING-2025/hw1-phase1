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
