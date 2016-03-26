from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/users")

def user_info(username):
	return api.call(username)

#requires authorization
def subscribed_to(username, channel):
	return api.call(username + "/subscriptions/" + channel)
	

uapi = TwitchAPI("api", extra_base="api/users")	

def followed_channels(username, **params):
	return uapi.call(username + "/follows/channels", **params)
	
def followed_games(username, **params):
	return uapi.call(username + "/follows/games", **params)