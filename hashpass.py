#! /usr/bin/python3

try:
	import os
	import re
	import hashlib	
	from hasher import *
except:
	print("Error, Unable to Import modules.")
	exit(1);

def getKey(password):
	return returnKey(password)

def addUser(username, password):
	if username not in users and password not in users:
		if validatePass(password):
			users.update({username : getKey(password)})
		else:
			print("Bad Password, please try again")
	else:
		print("User already exists")

def validateUser(username, password):
	if username in users:
		userpass = users.get(username)
		key = getKey(password)

		if userpass == key:
			print("Validated")
			return True			
		else:
			print("User not found or bad password")
			return False
	else:
		print("User not found")
		return False

def validatePass(password):
	l,u,p,d = 0,0,0,0
	if(len(password) >= 8):
		for i in password:
			if (i.islower()):
				l += 1
			if (i.isupper()):
				u += 1
			if (i.isdigit()):
				d += 1
			if(i == '@' or i == '$' or i == '_'):
				p += 1
	if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d ==len(password)):
		return True
	else:
		return False

		
addUser("marge","1234")
addUser("tod","12345")
addUser("tod","R@m@_f0rtu9e$")
validateUser("tod","R@m@_f0rtu9e$")

print(users)