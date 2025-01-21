# My solution2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = []
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    stack.append((i, j))
                    while stack:
                        y, x = stack.pop()
                        if 0 <= x + 1 < len(grid[0]) and grid[y][x + 1] == "1":
                            stack.append((y, x + 1))
                            grid[y][x + 1] = "0"
                        if 0 <= x - 1 < len(grid[0]) and grid[y][x - 1] == "1":
                            stack.append((y, x - 1))
                            grid[y][x - 1] = "0"
                        if 0 <= y + 1 < len(grid) and grid[y + 1][x] == "1":
                            stack.append((y + 1, x))
                            grid[y + 1][x] = "0"
                        if 0 <= y - 1 < len(grid) and grid[y - 1][x] == "1":
                            stack.append((y - 1, x))
                            grid[y - 1][x] = "0"
                    count += 1
        return count