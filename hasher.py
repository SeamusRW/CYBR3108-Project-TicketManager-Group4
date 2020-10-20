import os
import hashlib

salt = os.urandom(32)

users = {}

def returnKey(password):
	hashed = hashlib.pbkdf2_hmac(
		'sha256',
		password.encode('utf-8'),
		salt,
		100000,
		dklen = 128
		)
	
	return hashed