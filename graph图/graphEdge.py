from graphNode import Node

class Edge:
    def __init__(self, weight: int, ori: Node, dest: Node) -> None:
        self.weight = weight
        self.ori = ori
        self.dest = dest