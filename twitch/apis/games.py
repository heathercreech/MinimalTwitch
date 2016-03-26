from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/games")

def top_games(**params):
	return api.call("top", **params)