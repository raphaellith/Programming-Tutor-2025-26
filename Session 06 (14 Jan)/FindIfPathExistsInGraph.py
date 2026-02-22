from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialise union-find
        parent = [i for i in range(n)]
        weight = [1 for _ in range(n)]

        # Identifies root of tree containing i
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i

        # Union
        for edge in edges:
            u, v = edge
            u_root = root(u)
            v_root = root(v)
            if u_root == v_root:
                continue
            if weight[u_root] < weight[v_root]:  # u_root has a lighter tree, so it becomes the child of v_root
                parent[u_root] = v_root
                weight[v_root] += weight[u_root]
            else:
                parent[v_root] = u_root
                weight[u_root] += weight[v_root]

        return root(source) == root(destination)
