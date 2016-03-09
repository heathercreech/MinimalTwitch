import json
from os import urandom

from flask import Flask, session, escape, request, redirect, url_for, render_template

from api.followed import getLiveChannels, getPreviewImages, getStreamObjects
from api.stream import ChannelStream
from api.games import getTopGames, getGameStreams


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return redirect(url_for('following', username=request.form['username']))
	else:
		return render_template('login.html')

@app.route('/following/<username>')
def following(username):
	channels = getStreamObjects(getLiveChannels(username))
	#temp_channel = ChannelStream("witwix")
	#print(temp_channel.file_url + temp_channel.stream_filepaths[0])
	return render_template('index.html', channels=channels, username=username)

@app.route('/channel/<channel>')
def channel(channel):
	return render_template('channel.html', channel=channel)

@app.route('/games/')
def gameList():
	return render_template('games.html', game_list=getTopGames({'limit': 42}))

@app.route('/game/<game_name>')
def gameChannels(game_name = None):
	if game_name:
		return render_template('game.html', game_name=game_name, game_channels=getGameStreams({"game": game_name}))
	return redirect(url_for("gameList"))

#in case we use session in the future
def getSecretKey(filepath):
	try:
		with open(filepath) as sk_file:
			return sk_file.readline()
	except FileNotFoundError:
		generated_key = str(urandom(50))
		with open(filepath, 'w') as sk_file:
			sk_file.write(generated_key)
			return generated_key

def updateJinja(func):
	app.jinja_env.globals[func.__name__] = func
	
if __name__ == '__main__':
	app.secret_key = getSecretKey('secret_key.cfg')
	app.run(host='0.0.0.0')