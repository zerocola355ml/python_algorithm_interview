# My solution1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        seen = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = []
                if (i, j) not in seen:
                    seen.add((i, j))
                    if grid[i][j] == "1":
                        stack.append((i, j))
                        while stack:
                            y, x = stack.pop()
                            if (y, x + 1) not in seen and 0 <= x + 1 < len(grid[0]) and grid[y][x + 1] == "1":
                                stack.append((y, x + 1))
                                seen.add((y, x + 1))
                            if (y, x - 1) not in seen and 0 <= x - 1 < len(grid[0]) and grid[y][x - 1] == "1":
                                stack.append((y, x - 1))
                                seen.add((y, x - 1))
                            if (y + 1, x) not in seen and 0 <= y + 1 < len(grid) and grid[y + 1][x] == "1":
                                stack.append((y + 1, x))
                                seen.add((y + 1, x))
                            if (y - 1, x) not in seen and 0 <= y - 1 < len(grid) and grid[y - 1][x] == "1":
                                stack.append((y - 1, x))
                                seen.add((y - 1, x))
                        count += 1
        return count