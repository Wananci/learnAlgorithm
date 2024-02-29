class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.inNodeNum = 0 ## 入度：有多少个点指向该点
        self.outNodeNum = 0 ## 出度：这个点指向多少个点
        self.nexts = []  ## 存放指向的点
        self.edges = []  ## 出度的边：从该点指出去的边

        