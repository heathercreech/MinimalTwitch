from twitch.apis import users

channel_request_limit = 500


#gets a list of all the channels that a user follows
def getFollowedChannels(username):
	return users.followed_channels(username)["follows"]

#gets the live channels that a specific user follows
def getLiveChannels(username):
	followed_channels = getFollowedChannels(username)
	for channel in followed_channels:
		if channel["live"]:
			yield channel
			
#
def getStreamObject(channel_obj):
	stream_obj = channel_obj["stream"]
	if stream_obj is not None:
		return channel_obj["stream"]

def getStreamObjects(channels):
	for c in channels:
		yield getStreamObject(c)
		
#returns the large preview image for a live stream
def getPreviewImages(live_channels):
	for channel in live_channels:
		yield getStreamObject(channel)["preview"]["medium"]