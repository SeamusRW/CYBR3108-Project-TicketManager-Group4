# Gloves module for Ticket Manager, lets say frontend is the hands, backend is the shovel, and gloves are,
# well the gloves....
# gloves allows frontend to use functionality from backend without direct access to it. This allows for more checks to
#   be performed on incoming data and what not, pro tip: wearing gloves keeps your hands from getting dirty.
# To ensure proper functionality, please ensure all requirements are met, you can do this by reading the README either
#   in the provided zip file or our github. https://github.com/SeamusRW/CYBR3108-Project-TicketManager-Group4
# Also please ensure that all modules are in the same folder.
# Authors: John Walker, Roydon D'souza
# V 3.0
# Date: 11/11/2020

try:
    from backend import *
except:
    print("Cannot Import Modules...")
    exit(0)

loggedIN = False


def signup(username, password, fname, lname):  # calls the addUser function in backend to add a user to the database
    addUser(username, password, fname, lname)


def login(username, password):  # login function, this uses backend functions to validate the user, if its validated
    # then loggedIN is set to true and the user is able to login
    global loggedIN
    if validateUser(username, password) and not loggedIN:
        loggedIN = True
        return True
    else:
        return False


def signOut(username, password):
    # sets loggedIN to false, could have probably gotten rid of the redundant user and pass
    # params, but such is life amirite
    global loggedIN
    if loggedIN:
        loggedIN = False
    else:
        print("User already signed out")


def valPass(password):  # uses the validatePass function found in backend to, you guessed it, validate the password
    if validatePass(password):
        return True
    else:
        return False


def checkUser(username):  # uses the valUser function found in backend to, you guessed it, see if they user exists
    if valUser(username):
        return True
    else:
        return False


def addpoints(username, points):  # uses the update_points function in backend to update the points
    try:
        update_points(username, points)
    except:
        print("Error Adding points")
    else:
        print("Points added succesfully")


def getpointamnt(username):
    # returns the current amount of points found within the database, did you know it uses backend functions?
    try:
        points = select_points(username)
    except:
        print("Unable to retrieve point amount")
    else:
        return points


def update_tickets(user, mode):
    # sends which ticket the user wants to backend, mode select allows for population of specific cells in db
    # also it uses backend modules
    if mode == 1:
        update_t1(user)
    if mode == 2:
        update_t2(user)
    if mode == 3:
        update_t3(user)


def get_tickets(user, mode):
    # returns which ticket cells are populated within db, mode select allows for specific cells to be checked
    # surprise surprise, it uses backend functions.
    thing = ""

    if mode == 1:
        thing = check_t1(user)
    if mode == 2:
        thing = check_t2(user)
    if mode == 3:
        thing = check_t3(user)

    return thing
