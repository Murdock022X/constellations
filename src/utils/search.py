from fuzzywuzzy import process

class SearchUtils:

	@staticmethod
	def search(sky, query):
		names = ["dummy", "names"]
		results = process.extract(query, names)
		return results


