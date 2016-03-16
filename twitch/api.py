import requests

class TwitchAPI:
	
	def __init__(self, subdomain, extra_base=""):
		self.subdomain = ""
		self.base_url = "https://{0}.twitch.tv/{1}/".format(subdomain, extra_base)
	
	def call(self, path, **params):
		query_params = dict(as3='t', **params)
		url_target = self.base_url + path
		
		try:
			response = requests.get(url_target, params=query_params)
			if response.status_code == 404:
				raise requests.exceptions.HTTPError
				
			return response.json()
		except requests.exceptions.HTTPError as e:
			print("HTTPError: check your API path and make sure it is correct.\n	URL: " + url_target)
		except requests.exceptions.RequestException as e:
			print("Requests error: " + e)

			
class ChannelsAPI(TwitchAPI):
	
	def __init__(self):
		super().__init__("api", extra_base="kraken/channels")
		
	def channel_info(self, channel):
		return self.call(channel)
		
	def channel_videos(self, channel):
		return self.call(channel + "/videos")
	
	def channel_followers(self, channel):
		return self.call(channel + "/follows")
		
	#requires authorization
	def channel_editors(self, channel):
		return self.call(channel + "/editors")
		
		
class UndocumentedChannelsAPI(TwitchAPI):
	
	def __init__(self):
		super().__init__("api", extra_base="api/channels")
	
	def access_token(self, channel):
		return self.call(channel + "/access_token")
	
	def channel_info(self, channel):
		return self.call(channel)
	
	
class HostAPI(TwitchAPI):
	
	def __init__(self):
		super().__init__("tmi", extra_base="api/hosts")

		
if __name__ == "__main__":
	pass
	