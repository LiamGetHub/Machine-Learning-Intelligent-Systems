class MinimaxTree:
    def __init__(self, tree):
        self.__tree = tree
        self.__root = next(iter(tree))  

    def minimax_min(self):
        return self.__minimax_min(self.__root, float('-inf'), float('inf'))

    def minimax_max(self):
        return self.__minimax_max(self.__root, float('-inf'), float('inf'))

    def __minimax_min(self, node, alpha, beta):
        if isinstance(self.__tree[node][0], int):
            return self.__tree[node][0], [self.__tree[node][0]]

        best_value = float('inf')
        explored_leaves = []

        for child in self.__tree[node]:
            value, leaves = self.__minimax_max(child, alpha, beta)
            best_value = min(best_value, value)
            explored_leaves.extend(leaves)
            beta = min(beta, best_value)
            if alpha >= beta:
                break

        return best_value, explored_leaves

    def __minimax_max(self, node, alpha, beta):
        if isinstance(self.__tree[node][0], int):
            return self.__tree[node][0], [self.__tree[node][0]]

        best_value = float('-inf')
        explored_leaves = []

        for child in self.__tree[node]:
            value, leaves = self.__minimax_min(child, alpha, beta)
            best_value = max(best_value, value)
            explored_leaves.extend(leaves)
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break

        return best_value, explored_leaves

    def __str__(self):
        def preorder(node):
            if isinstance(self.__tree[node][0], int):
                return f"{node} {' '.join(map(str, self.__tree[node]))}"
            return f"{node} {' '.join(preorder(child) for child in self.__tree[node])}"
        
        return preorder(self.__root)