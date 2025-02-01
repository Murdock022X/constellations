from utils.constellation import Constellation, Node
from fuzzywuzzy import process

class SearchUtils:

	@staticmethod
	def search(sky: dict[str, Constellation], query: str):
		names = [c for c in sky.keys()]
		results = process.extract(query, names)
		return [sky[name[0]] for name in results]

