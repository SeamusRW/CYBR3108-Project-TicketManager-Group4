#Please make sure server.py, frontend.py, gloves.py, backend.py, UserInfo.sqlite are all in the same folder/path
#Please make sure you run server.py frist before you run frontend.py
#DO NOT RUN ME!!!!!!!!!!!!
#Writen by: Walker, John and D'souza, Roydon
#Date: 11 Nov 2020

try:
    import os
    import hashlib
    import sys
    import socket
    import sqlite3 as sql
    from sqlite3 import Error
except:
    print("Error, Unable to Import modules.")
    exit(1)

#Creating a TCP socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))

#Hashes Password with salt
def getKey(password):
    salt = os.urandom(32)
    hardenpassword(password, salt)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        b'password',
        b'salt',
        100000,
        dklen=128
    )
    hashed = hashed.hex()

    return hashed

#The hashed password is harden to increase security 
def hardenpassword(password, salt):
    harden = (password, salt)
    return harden


#Adds user, calls insert into
def addUser(username, password, fname, lname):

    if validatePass(password):
        insert_into(username, getKey(password), fname, lname, points=500, t1="None", t2="None", t3="None")
    else:
        print("Bad Password, please try again")


#Checks to see if user and password match
def validateUser(user, password):
    if select_user(user):
        if select_pass(user, password):
            print("Validated")
            return True
        else:
            print("Incorrect Password")
            return False
    else:
        print("User not found")
        return False

#Checks to see if password is correct
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

#Check is user is store in the SQLite
def valUser(user):
    if select_user(user):
        return True
    else:
        return False


#Here begins the frankenstein of 2 am sql code
def insert_into(user, password, fname, lname, points, t1, t2, t3):
    try:
        points = str(points)
        #SQL code
        payload = ''' INSERT INTO USERS (Username,Password,Fname,LName,Points,TICKETA,TICKETB,TICKETC) Values ({0},{1},{2},{3},{4},{5},{6},{7})'''.format("'" + user + "'", "'" + password + "'", "'" + fname + "'", "'" + lname + "'", "'" + points + "'", "'" + t1 + "'", "'" + t2 + "'", "'" + t3 + "'")
        #Code sent to server side
        client_socket.send(payload.encode('utf-8'))
        #Received data
        value = client_socket.recv(1024)
    except:
        print("Unknown Error")

#Retrieving user server (SQLite)
def select_user(user):
    try:
        #SQL code
        payload = ''' SELECT Username FROM USERS WHERE Username = {}'''.format("'" + user + "'")
        #Code sent to the server side
        client_socket.send(payload.encode('utf-8'))
        #Received data
        value = client_socket.recv(1024)
        #Data is decoded
        value = value.decode('utf-8')
        #Strip unwanted character from the data
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except:
        print("Unknown Error")
    else:
        if data == user:
            return True
        else:
            return False
        
#Retrieving password from that user server (SQLite)
def select_pass(user, password):
    try:
        payload = ''' SELECT Password FROM USERS WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except:
        print("Unknown Error")
    else:
        if getKey(password) == data:
            return True
        else:
            return False
        

#Here begins the horrifying amalgamation of last minute sql ideas
#Checking if ticket 1 is saved server (SQLite)
def check_t1(user):
    try:
        payload = ''' SELECT TICKETA FROM USERS WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except:
        print("Unknown Error")
    else:
        return data

#Checking if ticket 2 is saved server (SQLite)
def check_t2(user):
    try:
        payload = ''' SELECT TICKETB FROM USERS WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except:
        print("Unknown Error")
    else:
        return data

#Chekcing if ticket 3 is saved server (SQLite)
def check_t3(user):
    try:
        payload = ''' SELECT TICKETC FROM USERS WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except:
        print("Unknown Error")
    else:
        return data

#Updating ticket 1 server (SQLite)
def update_t1(user):
    try:
        payload = ''' UPDATE USERS SET TICKETA = '1' WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
    except:
        print("Unknown Error")

#Updating ticket 2 server (SQLite)
def update_t2(user):
    try:
        payload = ''' UPDATE USERS SET TICKETB = '1' WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
    except:
        print("Unknown Error")

#Updating ticket 3 server (SQLite)
def update_t3(user):
    try:
        payload = ''' UPDATE USERS SET TICKETC = '1' WHERE Username = {}'''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
    except:
        print("Unknown Error")
        
#Update the new points server (SQLite)
def update_points(user, points):
    try:
        payload = '''UPDATE USERS SET Points = {0} WHERE Username = {1}'''.format("'" + points + "'", "'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
    except:
        print("Unknown Error")

#Getting the points from the server (SQLite)
def select_points(user):
    try:
        payload = '''SELECT Points FROM USERS WHERE Username = {} '''.format("'" + user + "'")
        client_socket.send(payload.encode('utf-8'))
        value = client_socket.recv(1024)
        value = value.decode('utf-8')
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
        data = int(data)
    except:
        print("Unknown Error")
    else:
        return data
