from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/search")

def channels(query, **params):
	return api.call("channels", query=query, **params)

def streams(query, **params):
	return api.call("streams", query=query, **params)
	
def games(query, **params):
	return api.call("games", query=query, **params)