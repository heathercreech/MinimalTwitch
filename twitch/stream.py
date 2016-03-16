import requests


def getChannelAccessToken(channel_name):
	return requests.get("https://api.twitch.tv/api/channels/" + channel_name + "/access_token").json()

def parseManifestFile(resp_text):
	resp_text = resp_text.split("\n")
	for line in resp_text[:]:
		if not line or line[0] == '#':
			resp_text.remove(line)
	return resp_text
	
def mapLinksToQuality(quality_links):
	quality_strings = ["source", "high", "medium", "low", "mobile"]
	di = {}
	
	for x in range(0, len(quality_links)):
		di[quality_strings[x]] = quality_links[x]
	return di
	
def getChannelQualityLinks(channel_name, access_token):
	usher_url = "http://usher.twitch.tv/api/channel/hls/" + channel_name + ".m3u8"
	payload = {"sig": access_token["sig"], "token": access_token["token"], "allow_source": "true"}
	return parseManifestFile(requests.get(usher_url, params=payload).text)
	
def getQualityMappedLinks(channel_name):
	quality_links = getChannelQualityLinks(channel_name, getChannelAccessToken(channel_name))
	return mapLinksToQuality(quality_links)

def getStreamFilepaths(quality_link):
	return parseManifestFile(requests.get(quality_link).text)


class ChannelStream:
	def __init__(self, channel_name):
		self.channel_name = channel_name
		self.quality_links = getQualityMappedLinks(channel_name)
		
		self.file_url = self.quality_links["source"][:self.quality_links["source"].rfind('/')+1]
		
		self.stream_filepaths = getStreamFilepaths(self.quality_links["source"])
		
	
	def updateFilepaths():
		pass
	