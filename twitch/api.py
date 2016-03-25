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
		except requests.exceptions.HTTPError as e:
			print("HTTPError: check your API path and make sure it is correct.\n	URL: " + url_target)
		except UnsupportedMethodError:
			print("Method supplied to TwitchAPI.call is not supported: " + method)
		except requests.exceptions.RequestException as e:
			print("Requests error: " + e)
		

#provides operations for a user's block list
class BlocksAPI:
	api = TwitchAPI("api", extra_base="kraken/users")
	
	#requires authorization
	@staticmethod
	def block_list(username):
		return BlocksAPI.api.call(username + "/blocks")
	
	#requires authorization
	@staticmethod
	def block_user(username, target):
		return BlocksAPI.api.call(username + "/blocks/" + target, method="PUT")
	
	#requires authorization
	@staticmethod
	def unblock_user(username, target):
		return BlocksAPI.api.call(username + "/blocks/" + target, method="DELETE")
		
		
class ChannelsAPI:
	api = TwitchAPI("api", extra_base="kraken/channels")
	
	@staticmethod
	def channel_info(channel):
		return ChannelsAPI.api.call(channel)
	
	@staticmethod
	def channel_videos(channel):
		return ChannelsAPI.api.call(channel + "/videos")
	
	@staticmethod
	def channel_followers(channel):
		return ChannelsAPI.api.call(channel + "/follows")

	#requires authorization
	@staticmethod
	def channel_editors(channel):
		return ChannelsAPI.api.call(channel + "/editors")
	
	#requires authorization
	@staticmethod
	def update_channel(channel, **params):
		return ChannelsAPI.api.call(channel, method="PUT", **params)
	
	#requires authorization
	@staticmethod
	def reset_stream_key(channel):
		return ChannelsAPI.api.call(channel + "/stream_key", method="DELETE")
		
	#requires authorization
	@staticmethod
	def run_commercial(channel, **params):
		return ChannelsAPI.api.call(channel + "/commercial", method="POST", **params)
	
	@staticmethod
	def get_teams(channel):
		return ChannelsAPI.api.call(channel + "/teams")
	
		
class UChannelsAPI:
	api = TwitchAPI("api", extra_base="api/channels")
	
	@staticmethod
	def access_token(channel):
		return UChannelsAPI.api.call(channel + "/access_token")

	def channel_info(channel):
		return UChannelsAPI.api.call(channel)
	
	
class HostAPI:
	api = TwitchAPI("tmi", extra_base="api/hosts")

		
if __name__ == "__main__":
	print(ChannelsAPI.run_commercial("witwix"))
	