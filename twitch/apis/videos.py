from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/videos")

def get_video(id):
	return api.call(id)
	
def top(**params):
	return api.call("top", **params)
	
#requires authorization
def followed(**params):
	return api.call("followed")