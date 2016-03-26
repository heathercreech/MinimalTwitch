import requests


class UnsupportedMethodError(requests.exceptions.RequestException):
	"""Supplied method wasn't supported"""

	
class TwitchAPI:
	
	def __init__(self, subdomain, extra_base=""):
		self.subdomain = ""
		self.base_url = "https://{0}.twitch.tv/{1}/".format(subdomain, extra_base)

	def call(self, path, method="GET", **params):
		query_params = dict(as3='t', **params)
		url_target = self.base_url + path

		try:
			if method == "GET":
				response = requests.get(url_target, params=query_params)
			elif method == "PUT":
				response = requests.put(url_target, data=query_params)
			elif method == "DELETE":
				response = requests.delete(url_target, data=query_params)
			elif method == "POST":
				response = requests.post(url_target, data=query_params)
			else:
				raise UnsupportedMethodError
			
			if response.status_code == 404:
				raise requests.exceptions.HTTPError
			
			return response.json()
		except requests.exceptions.HTTPError:
			print("HTTPError: check your API path and make sure it is correct.\n	URL: " + url_target)
		except UnsupportedMethodError:
			print("Method supplied to TwitchAPI.call is not supported: " + method)
		except requests.exceptions.RequestException as e:
			print("Requests exception in TwitchAPI.call: " + e)
		except Exception as e:
			print("Exception in TwitchAPI.call: " + e)

			
if __name__ == "__main__":
	print(ChannelsAPI.run_commercial("witwix"))
	