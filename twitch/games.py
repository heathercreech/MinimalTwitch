import requests
import sys


def getTopGames(params={}):
	return requests.get('https://api.twitch.tv/kraken/games/top', params).json()['top']

def getGameStreams(params={}):
	return requests.get('https://streams.twitch.tv/kraken/streams', params).json()['streams']
	
if __name__ == '__main__':
	pass