from graphNode import Node
from graphEdge import Edge
from typing import Dict, List

class graph:
    def __init__(self, nodes: Dict[int, Node], edges: List[Edge]) -> None:
        self.nodes = nodes ## node = {int 表示点的序号: Node 节点}  
        self.edges = edges
