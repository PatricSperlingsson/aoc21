#https://adventofcode.com/2024/day/10
import numpy as np
from collections import deque, defaultdict
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('10i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
grid = []
for line in lines:
    grid.append([int(char) for char in line])
print("grid:", grid)

rows = len(lines)
cols = len(lines[0])
print(f"rows: {rows}")
print(f"cols: {cols}")

# Map of trailheads
trailhead_starts = []
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 0:
            trailhead_starts.append((row, col))
print(f"trailhead_starts: {trailhead_starts}")

#             Up       Down    Left     Right
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Simulate trailheads
reachable_nines = defaultdict(list)

total_visited_nines = 0
for x, y in trailhead_starts:
    print(f"x, y: {x}, {y}")
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        current_height = grid[x][y]
        print(f"current_height: {current_height}")

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == current_height + 1:
                    queue.append((nx, ny))
                    if grid[nx][ny] == 9:
                        reachable_nines[(x, y)].append((nx, ny))

sum_ratings = 0
#   Key        list
for trailhead, nines in reachable_nines.items():
    print(f"Trailhead {trailhead} can reach nines at: {nines}")
    sum_ratings += len(nines)
print(f"sum_ratings: {sum_ratings}")
# Corrects answer: 1252