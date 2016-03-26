from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/chat")

def badges(channel):
	return api.call(channel + "/badges")

def emoticons():
	return api.call("emoticons")

def emoticon_images():
	return api.call("emoticon_images")
	