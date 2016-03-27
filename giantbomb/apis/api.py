import requests

def load_api_key(filepath):
	gb_api_key = ""
	with open(filepath, "r") as key_file:
		gb_api_key = key_file.readline()
	return gb_api_key

	
class GiantBombAPI:
	api_key = load_api_key("gb_api_key.secret")
	
	def __init__(self, endpoint):
		self.base_url = "http://www.giantbomb.com/api/{0}/".format(endpoint)
		self.request_headers = {"User-Agent": "Seth Creech"}
		
	def call(self, path, format="json", **params):
		query_params = dict(api_key=GiantBombAPI.api_key, format=format, **params)
		url_target = self.base_url + path
		try:
			response = requests.get(url_target, headers=self.request_headers, params=query_params)

			if response.status_code == 404:
				raise requests.exceptions.HTTPError
			
			return response.json()["results"]
		except requests.exceptions.HTTPError:
			print("HTTPError: check your API path and make sure it is correct.\n	URL: " + url_target)
		except requests.exceptions.RequestException as e:
			print("Requests exception in GiantBombAPI.call:\n\t", e)
		except Exception as e:
			print("Exception in GiantBombAPI.call:\n\t", e)
			

if __name__ == "__main__":
	print(GiantBombAPI("game/3030-49884").call(field_list="expected_release_year,expected_release_month,expected_release_day"))