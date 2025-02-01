import os.path

class Node:
    def __init__(self, filename):
        self.filename = filename
        self.edges = set()

    def __str__(self):
        return "{} -> ".format(self.filename) + ",".join([str(edge) for edge in self.edges])
    
    __repr__ = __str__

    def add_edge(self, edge):
        self.edges.add(edge)

class Edge:
    def __init__(self, node: Node, annotation: str, correlation_color: str):
        self.node = node
        self.annotation = annotation
        self.color = correlation_color

    def __str__(self):
        return "Edge to: {}, anno: {}, color: {}".format(self.node.filename, self.annotation, self.color)

    __repr__ = __str__

class Constellation:
    def __init__(self, name: str, yaml_dict: dict):
        self.name = name
        self.vertices: dict = {}

        for vertex_filename, edges in yaml_dict.items():
            self.vertices[vertex_filename] = Node(vertex_filename)


        for vertex_filename, edges in yaml_dict.items():
            src_node: Node = self.vertices[vertex_filename]

            if edges is not None:
                for dst_file, attrs in edges.items():
                    dst_node: Node = self.get_star(dst_file)
                    self.add_edge(src_node, dst_node, attrs[0], attrs[1])

    def add_star(self, name: str):
        assert(name not in self.vertices.keys())
        self.vertices[name] = Node(name)
    
    def add_edge(self, source_star: Node, dest_star: Node, comment: str, color: str):
        assert(source_star.filename in self.vertices.keys())
        assert(dest_star.filename in self.vertices.keys())
        edge = Edge(dest_star, comment, color)
        source_star.add_edge(edge)

    def get_star(self, name: str) -> Node:
        return self.vertices[name]

    def get_all_stars(self) -> list[Node]:
        return self.vertices
    
    def traverse_files(self, dir: str, ignore_ext=[]):
        assert(os.path.isdir(dir))
        dirs = list(os.walk(dir, followlinks=False))
        for sub in dirs:
            if sub[2]:
                for fname in sub[2]:
                    ext = fname.split('.').pop()
                    if not ext in ignore_ext:
                        self.add_star(fname)




