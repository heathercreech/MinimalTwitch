from twitch.apis import games, streams

def getTopGames(**params):
	return games.top_games(**params)['top']

def getGameStreams(game, **params):
	return streams.list(game=game, **params)["streams"]