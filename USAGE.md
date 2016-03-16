#Usage

##Entry Point: `twitch.sethcreech.me`
The entry point is a simple page that requests the users Twitch username. After the user submits their username, they are redirected to a list of their followed channels.

##Following: `twitch.sethcreech.me/following/<username>`
Requests and displays <username>'s list of followed channels. In time, this will become the main page, where navigation to the rest of the site will be possible.

##Channel: `twitch.sethcreech.me/channel/<channel>`
Requests and displays the stream from <channel>. The current web player is not Twitch's embedded version. Instead, the application uses Twitch.video.Player() supplied from (I believe... I didn't look very closely at the source) `player.twitch.tv/js/player.e3985a71.js`. This allows heavy customization of the player's UI for minimalistic purposes.