from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/channels")

def channel_info(channel):
	return api.call(channel)

def channel_videos(channel):
	return api.call(channel + "/videos")

def channel_followers(channel):
	return api.call(channel + "/follows")

#requires authorization
def channel_editors(channel):
	return api.call(channel + "/editors")

#requires authorization
def update_channel(channel, **params):
	return api.call(channel, method="PUT", **params)

#requires authorization
def reset_stream_key(channel):
	return api.call(channel + "/stream_key", method="DELETE")
	
#requires authorization
def run_commercial(channel, **params):
	return api.call(channel + "/commercial", method="POST", **params)

def get_teams(channel):
	return api.call(channel + "/teams")

#requires authorization
def subscribers(channel, **params):
	return api.call(channel + "/subscriptions", **params)

#requires authorization
def has_subscriber(channel, username):
	return api.call(channel + "/subscriptions/" + username)

	
uapi = TwitchAPI("api", extra_base="api/channels")

def access_token(channel):
	return uapi.call(channel + "/access_token")
