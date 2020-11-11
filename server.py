#Please make sure server.py, frontend.py, gloves.py, backend.py, UserInfo.sqlite are all in the same folder/path
#Please make sure you run me frist before you run frontend.py
#Please please read readme first before doing anything!!!
#Welcome to the awesome server side code!
#Writen by: D'souza, Roydon and Walker, John
#Date: 11 Nov 2020


import socket
import sqlite3
from sqlite3 import Error

# Connecting to SQLite
conn = sqlite3.connect("UserInfo.sqlite")
c = conn.cursor()

#Creating a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))

#Listening or waiting for the client side to connect
server_socket.listen(5)

while True:
    #Server waiting for connection to the client.
    print("Server waiting for connection...")
    
    #Once connected the server display who its connected too.
    client_socket,addr = server_socket.accept()
    print("Client connected from",addr)
    
    while True:
        #reciving data from the client
        data = client_socket.recv(1024)     
        if not data or data.decode('utf-8')=='END':            
            break
        #the received dat is decoded
        data = data.decode('utf-8')
        #coverting bytes to str
        data = str(data)[2:-1]

        #Fetching data from SQLite and sending it back to client
        try:
            #Executing the SQL code taht is received from client
            c.execute(data)
            sending = c.fetchone()
            payload = str(sending)
            #Sending the data back to client
            client_socket.send(payload.encode('utf-8'))
        except Error as e:
            print(e)
        finally:
            conn.commit()
    #Closing the socket
    client_socket.close()

