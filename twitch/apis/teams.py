from .api import TwitchAPI


api = TwitchAPI("tmi", extra_base="kraken/teams")

def list(**params):
	return api.call("", **params)
	
def get_team(team):
	return api.call(team)