from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/ingests")

def list():
	return api.call("")