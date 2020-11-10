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

file = "UserInfo.sqlite"
conn = sql.connect(file)
c = conn.cursor()


# Hashes Password
def getKey(password):
    salt = os.urandom(32)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        b'password',
        b'salt',
        100000,
        dklen=128
    )
    hashed = hashed.hex()

    return hashed


# adds user, calls insert into
def addUser(username, password, fname, lname):
    # if username not in users and password not in users:
    if validatePass(password):
        insert_into(username, getKey(password), fname, lname, points=500, t1="None", t2="None", t3="None")
    else:
        print("Bad Password, please try again")


# checks to see if user and password match
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


def valUser(user):
    if select_user(user):
        return True
    else:
        return False


# here begins the frankenstein of 2 am sql code
def insert_into(user, password, fname, lname, points, t1, t2, t3):
    try:
        points = str(points)
        c.execute(
            ''' INSERT INTO USERS (Username,Password,Fname,LName,Points,TICKETA,TICKETB,TICKETC)
                        Values (?,?,?,?,?,?,?,?);''', (user, password, fname, lname, points, t1, t2, t3))
    except sql.Error as e:
        print(e)
    except TypeError as e:
        print(e)
    except:
        print("Unknown Error")
    finally:
        conn.commit()


def select_user(user):
    try:
        c.execute(
            ''' SELECT Username FROM USERS WHERE Username = {}
        '''.format("'" + user + "'"))
        value = c.fetchone()
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
        print(data)
    except sql.Error as e:
        print(e)
    except:
        print("Unknown Error")
    else:
        if data == user:
            return True
        else:
            return False
    finally:
        conn.commit()


def select_pass(user, password):
    try:
        c.execute(''' SELECT Password FROM USERS WHERE Username = {}
        '''.format("'" + user + "'"))
        value = c.fetchone()
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
        print(data)
    except sql.Error as e:
        print(e)
    else:
        print(getKey(password))
        if getKey(password) == data:
            return True
        else:
            return False
    finally:
        conn.commit()


# here begins the horrifying amalgamation of last minute sql ideas
def check_t1(user):
    try:
        c.execute(''' SELECT TICKETA FROM USERS WHERE Username = {}
           '''.format("'" + user + "'"))
        value = c.fetchone()
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except sql.Error as e:
        print(e)
    else:
        return data
    finally:
        conn.commit()


def check_t2(user):
    try:
        c.execute(''' SELECT TICKETB FROM USERS WHERE Username = {}
           '''.format("'" + user + "'"))
        value = c.fetchone()
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except sql.Error as e:
        print(e)
    else:
        return data
    finally:
        conn.commit()


def check_t3(user):
    try:
        c.execute(''' SELECT TICKETC FROM USERS WHERE Username = {}
           '''.format("'" + user + "'"))
        value = c.fetchone()
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
    except sql.Error as e:
        print(e)
    else:
        return data
    finally:
        conn.commit()


def update_t1(user):
    try:
        c.execute(''' UPDATE USERS SET TICKETA = '1' WHERE Username = ?
           ''', [user])
    except sql.Error as e:
        print(e)
    finally:
        conn.commit()


def update_t2(user):
    try:
        c.execute(''' UPDATE USERS SET TICKETB = '1' WHERE Username = ?
           ''', [user])
    except sql.Error as e:
        print(e)
    finally:
        conn.commit()


def update_t3(user):
    try:
        c.execute(''' UPDATE USERS SET TICKETC = '1' WHERE Username = ?
           ''', [user])
    except sql.Error as e:
        print(e)
    finally:
        conn.commit()


def update_points(user, points):
    try:
        c.execute('''UPDATE USERS SET Points = {0} WHERE Username = {1}
            '''.format("'" + points + "'", "'" + user + "'"))
    except sql.Error as e:
        print(e)
    except:
        print("Unknown Error")
    finally:
        conn.commit()


def select_points(user):
    try:
        c.execute('''SELECT Points FROM USERS WHERE Username = {} '''.format("'" + user + "'"))
        value = c.fetchone()
        data = "{}".format(value).translate({ord(i): None for i in "(')[],"})
        points = int(data)
    except sql.Error as e:
        print(e)
    except:
        print("Unknown Error")
    else:
        return points
    finally:
        conn.commit()
