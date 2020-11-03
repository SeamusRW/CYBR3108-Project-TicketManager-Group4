import socket
import sqlite3
from sqlite3 import Error


class Server:
    file = "UserInfo.sqlite"
    conn = sqlite3.connect(file)
    c = conn.cursor()

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        totalsent = 0

        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("<<Server connection broken")
            totalsent = totalsent + sent

    def recv(self):
        chunks = []
        bytes_recd = 0

        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunck == b'':
                raise RuntimeError("<<Server connection broken>>")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


def adduser(username, password, fname, lname, points):
    try:
        c.execute(
            ''' INSERT INTO User ({0},{1},{2},{3},{4}) 
            '''.format(username, password, fname, lname, points))
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.commit()


def getuser(uname):
    try:
        c.execute(
            ''' SELECT * FROM Users WHERE {0} = {1}
            '''.format(username, uname))
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.commit()


def getpass(username):
    try:
        c.execute(
            ''' SELECT password FROM User WHERE username = {} 
            '''.format(username))
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.commit()