import yaml
from constellation import Constellation

with open("data/sample.yml") as f:
    y = yaml.safe_load(f)

c = Constellation("name", y["my_constellation"])