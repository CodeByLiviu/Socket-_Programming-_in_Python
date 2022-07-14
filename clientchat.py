import socket
import sys
import errno


HEADER_LENGTH = 10
PORT = 8000
SERVER = "192.168.0.113"
ADDR = (SERVER, PORT)
PROTOCOL = 'utf-8'

myUsername = input("Username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.setblocking(False)

username = myUsername.encode(PROTOCOL)
usernameHeader = f"{len(username):<{HEADER_LENGTH}}".encode(PROTOCOL)
client.send(usernameHeader + username)

while True:
    message = input(f"{myUsername} > ")
    if message:
        message = message.encode(PROTOCOL)
        messageHeader = f"{len(message):<{HEADER_LENGTH}}".encode(PROTOCOL)
        client.send(messageHeader + message)
    try:
        while True:
            usernameHeader = client.recv(HEADER_LENGTH)
            if not len(usernameHeader):
                print("Connection closed by the server")
                sys.exit()
            usernameLength = int(usernameHeader.decode(PROTOCOL).strip())
            username = client.recv(usernameLength).decode(PROTOCOL)

            messageHeader = client.recv(HEADER_LENGTH)
            messageLength = int(messageHeader.decode(PROTOCOL).strip())
            message = client.recv(messageLength).decode(PROTOCOL)

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("Reading error",str(e))
            sys.exit()
        continue

    except Exception as e:
        print('Generic error', str(e))
        sys.exit()






