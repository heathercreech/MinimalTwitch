from twitch.apis import games, streams
import giantbomb.apis.game 


cached_release_dates = {}

def getTopGames(**params):
	return games.top_games(**params)['top']

def getGameStreams(game, **params):
	return streams.list(game=game, **params)["streams"]
	
def getGiantBombID(game):
	return game["game"]["giantbomb_id"]
	
def getReleaseDate(id):
	
	if id in cached_release_dates:
		return cached_release_dates[id]
	
	game_release_date = giantbomb.apis.game.release_date(id)
	cached_release_dates[id] = game_release_date
	return game_release_date