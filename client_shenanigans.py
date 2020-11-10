import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1500))


def client1(payload):
    try:
        while True:
            client_socket.send(payload.encode('utf-8'))
            data = client_socket.recv(1024)
            print(str(data))
            break
    except KeyboardInterrupt:
        print("Exited by user")
    finally:
        client_socket.close()


def main():
    insert_into('tod', '1234123412341234', 'tod', 'tod', '500', 'None', 'None', 'None')


def insert_into(user, password, fname, lname, points, t1, t2, t3):
    try:
        points = str(points)
        data = ''' INSERT INTO USERS (Username,Password,Fname,LName,Points,TICKETA,TICKETB,TICKETC)"
                         Values (?,?,?,?,?,?,?,?); ''', (user, password, fname, lname, points, t1, t2, t3)
        payload = "{}".format(data)
        client1(payload)
    except sql.Error as e:
        print(e)
    except TypeError as e:
        print(e)
    except:
        print("Unknown Error")
    finally:
        conn.commit()
