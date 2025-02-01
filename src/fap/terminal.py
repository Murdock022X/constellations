from utils.constellation import Constellation
import argparse
import yaml
import os

def construct_constellation(dir: str, name: str, output: str):
    if os.path.exists(output):
        print("File alrady exists: ", output)
        return
    
    c = Constellation(name, {})
    c.traverse_files(dir)
    with open(output, 'x') as f:
        f.write(c.to_yaml())
    f.close()

def main(args):
    construct_constellation(args.directory, args.name, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Constellation Creator", description="Create a constellation yml file", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--directory')
    parser.add_argument('-n', '--name')
    parser.add_argument('-o', '--output', default="const.yml")
    args = parser.parse_args()
    main(args)
