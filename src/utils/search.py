from utils.constellation import Constellation
from fuzzywuzzy import process

class SearchUtils:

	@staticmethod
	def search(sky, query):
		names = [c.name for c in sky]
		results = process.extract(query, names)
		return results

