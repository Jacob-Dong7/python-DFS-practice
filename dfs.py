class DFS:
    def __init__(self):
        self.adj = [
            [1, 2, 3],        # 0 connected to 1,2,3
            [0, 4, 5],        # 1 connected to 0,4,5
            [0, 5, 6],        # 2 connected to 0,5,6
            [0, 6],           # 3 connected to 0,6
            [1, 7],           # 4 connected to 1,7
            [1, 2, 7, 8],     # 5 connected to 1,2,7,8
            [2, 3, 8],        # 6 connected to 2,3,8
            [4, 5, 9],        # 7 connected to 4,5,9
            [5, 6, 9],        # 8 connected to 5,6,9
            [7, 8]            # 9 connected to 7,8
            ]
        size = len(self.adj)
        if size <= 0:
            print("List empty")
            return
        
        self.visited = [False] * size
        self.traversal = []
    
    def run_algorithm(self):
        self.dfs(0)
    
    def dfs(self, curr):
        if self.visited[curr] == False:
            self.visited[curr] = True
            self.traversal.append(curr)
            for neighbour in self.adj[curr]:
                if self.visited[neighbour] == False:
                    self.dfs(neighbour)
                else:
                    continue



    def print_traversal(self):
        for node in self.traversal:
            if node == self.traversal[len(self.traversal) - 1]:
                print(node)
            else:
                print(node, end=" -> ")

