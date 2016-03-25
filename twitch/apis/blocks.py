import requests

from .api import TwitchAPI


api = TwitchAPI("api", extra_base="kraken/users")

#requires authorization
def block_list(username):
	return api.call(username + "/blocks")

#requires authorization
def block_user(username, target):
	return api.call(username + "/blocks/" + target, method="PUT")

#requires authorization
def unblock_user(username, target):
	return api.call(username + "/blocks/" + target, method="DELETE")

		
if __name__ == "__main__":
	print(block_list("witwix"))
	