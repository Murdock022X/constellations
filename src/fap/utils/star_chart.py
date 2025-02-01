from utils.constellation import Constellation, Node
import os.path

class StarChart:

    def __init__(self, name: str, constellations: dict[str, Constellation]={}, base_dir: str=None):
        self.name = name
        self.constellations = constellations # will be sky
        self.base_dir=base_dir
    
    def set_base_dir(self, base_dir: str):
        self.base_dir = base_dir
    
    def paths_valid(self) -> bool:
        for _, c in self.constellations.items():
            star: Node
            for star in c.get_all_stars():
                if not os.path.isfile(star.filename):
                    return False
            
        return True


    def save(self):
        pass
