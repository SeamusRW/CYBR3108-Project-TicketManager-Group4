try:
    from backend import *
except:
    print("Cannot Import Modules...")
    exit(1)

loggedIN = False


def signup(username, password, fname, lname):
    addUser(username, password, fname, lname)


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


def addpoints(username, points):
    try:
        update_points(username, points)
    except:
        print("Error Adding points")
    else:
        print("Points added succesfully")


def getpointamnt(username):
    try:
        points = select_points(username)
    except:
        print("Unable to retrieve point amount")
    else:
        return points


def update_tickets(user, mode):
    if mode == 1:
        update_t1(user)
    if mode == 2:
        update_t2(user)
    if mode == 3:
        update_t3(user)


def get_tickets(user, mode):
    if mode == 1:
        data = check_t1(user)
    if mode == 2:
        data = check_t2(user)
    if mode == 3:
        data=check_t3(user)

    return data
