try:
    import os
    import hashlib
    import sys
    import socket
except:
    print("Error, Unable to Import modules.")
    exit(1)


def getKey(password):
    salt = os.urandom(32)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000,
        dklen=128
    )

    return hashed


def addUser(username, password):
    if username not in users and password not in users:
        if validatePass(password):
            users.update({username: getKey(password)})
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
    l, u, p, d = 0, 0, 0, 0
    if len(password) >= 8:
        for i in password:
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if i.isdigit():
                d += 1
            if i == '@' or i == '$' or i == '_':
                p += 1
    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(password):
        return True
    else:
        return False


def valUser(username):
    if username in users:
        return True
    else:
        return False


users = {}
