
class Node:
    def __init__(self, filename):
        self.filename = filename
        self.edges = set()

    def add_edge(self, edge):
        self.edges.add(edge)

class Edge:
    def __init__(self, node: Node, annotation: str, correlation_color: str):
        self.node = node
        self.annotation = annotation
        self.color = correlation_color

class Constellation:
    def __init__(self, yaml_dict):
        self.vertices = {}

        for vertex_filename, edges in yaml_dict.items():
            self.vertices[vertex_filename] = Node(vertex_filename)

        for vertex_filename, edges in yaml_dict.items():
            src_node: Node = self.vertices[vertex_filename]

            for edge in edges:
                dst_node: Node = self.vertices[edge[0]]
                edge = Edge(dst_node, edge[1], edge[2])
                src_node.add_edge(edge)
