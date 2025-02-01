
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
    def __init__(self, name: str, yaml_dict: dict):
        self.name = name
        self.vertices: dict = {}

        for vertex_filename, edges in yaml_dict.items():
            self.vertices[vertex_filename] = Node(vertex_filename)

        for vertex_filename, edges in yaml_dict.items():
            src_node: Node = self.vertices[vertex_filename]

            for dst_file, attrs in edges.items():
                dst_node: Node = self.vertices[dst_file]
                edge = Edge(dst_node, attrs[0], attrs[1])
                src_node.add_edge(edge)
