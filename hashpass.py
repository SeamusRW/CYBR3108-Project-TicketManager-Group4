#! /usr/bin/python3

try:
	import os
	print("OS imported")
	import hashlib
	print("hashlib imported")
	from hasher import *
	print("hasher imported")
except:
	print("Error, Unable to Import modules.")
	exit(1);

def getKey(password):
	return returnKey(password)

def addUser(username, password):
	if username not in users and password not in users:
		users.update({username : getKey(password)})
	else:
		print("User already exists")

def validateUser(username, password):
	if username in users:
		userpass = users.get(username)
		key = getKey(password)

		if userpass == key:
			return True			
		else:
			return False
	else:
		print("User not found")
		return False