from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        parent: dict[tuple[int, int], tuple[int, int]] = dict()  # Key: (x, y)
        weight: dict[tuple[int, int], int] = dict()  # Key: (x, y)

        m = len(grid)
        n = len(grid[0])

        # Initialise
        for y in range(m):
            for x in range(n):
                if grid[y][x]:  # If this is land
                    parent[(x, y)] = (x, y)
                    weight[(x, y)] = 1

        def root(x, y):
            while (x, y) != parent[(x, y)]:
                x, y = parent[(x, y)]
            return x, y

        for y in range(m):
            for x in range(n):
                if not grid[y][x]:  # If this is sea, ignore
                    continue

                neighbours = self.getNeighbouringCells(x, y, m, n)
                neighbours = [(x, y) for x, y in neighbours if grid[y][x]]  # Filter out ocean

                for neighbour in neighbours:
                    # Union with neighbour
                    current_cell_root = root(x, y)
                    neighbour_root = root(*neighbour)
                    if current_cell_root == neighbour_root:
                        continue
                    if weight[current_cell_root] < weight[neighbour_root]:
                        parent[current_cell_root] = neighbour_root
                        weight[neighbour_root] += weight[current_cell_root]
                    else:
                        parent[neighbour_root] = current_cell_root
                        weight[current_cell_root] += weight[neighbour_root]

        max_weight = 0
        for land_cell in parent:
            if parent[land_cell] == land_cell:  # Root
                max_weight = max(max_weight, weight[land_cell])

        return max_weight

    def getNeighbouringCells(self, x: int, y: int, m: int, n: int) -> list[tuple[int, int]]:
        neighbours: list[tuple[int, int]] = []

        if x != 0:
            neighbours.append((x - 1, y))
        if x != n - 1:
            neighbours.append((x + 1, y))
        if y != 0:
            neighbours.append((x, y - 1))
        if y != m - 1:
            neighbours.append((x, y + 1))

        return neighbours
