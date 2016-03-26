from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/streams")

def list(**params):
	return api.call("", **params)

def channel_stream(channel):
	return api.call(channel)
	
def featured_streams(**params):
	return api.call("featured", **params)
	
def summary(**params):
	return api.call("summary", **params)