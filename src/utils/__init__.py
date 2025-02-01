
class Node:
    def __init__(self, filename, annotation, correlation_color):
        self.filename = filename

        self.annotation = annotation

        self.color = correlation_color

        self.edges = []

class Constellation:
    def __init__(self):
        self.vertices = {}
