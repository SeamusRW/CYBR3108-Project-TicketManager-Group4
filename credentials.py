try:
    from hashpass import *
except:
    print("Cannot Import Modules...")
    exit(1)

loggedIN = True


def signup(username, password):
    addUser(username, password)


def login(username, password):
    global loggedIN
    if validateUser(username, password) and not loggedIN:
        loggedIN = True
        return True
    else:
        return False


def signOut(username, password):
    global loggedIN
    if loggedIN:
        loggedIN = False
    else:
        print("User already signed out")


def valPass(password):
    if validatePass(password):
        return True
    else:
        return False


def checkUser(username):
    if valUser(username):
        return True
    else:
        return False
