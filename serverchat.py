import socket
import select

HEADER_LENGTH = 10
PORT = 8000
MY_HOST_NAME = socket.gethostname()
SERVER = socket.gethostbyname(MY_HOST_NAME)
ADDR = (SERVER, PORT)
PROTOCOL = 'utf-8'




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
print(f'[LISTENING] server is listening on {ADDR}')
server.listen()

socketList = [server]
clients = {}


def receiveMessage(client):
    try:
        messageHeader = client.recv(HEADER_LENGTH)
        if not len(messageHeader):
            return False
        messageLength = int(messageHeader.decode(PROTOCOL).strip())
        return {"header": messageHeader, "data": client.recv(messageLength)}

    except:
        return False


while True:
    readSockets, _, exceptionSockets = select.select(socketList, [], socketList)

    for notifiedSocket in readSockets:
        if notifiedSocket == server:
            client, clientAddress = server.accept()
            user = receiveMessage(client)
            if user is False:
                continue
            socketList.append(client)
            clients[client] = user
            print(f"Accepted new connection from {clientAddress[0]}:{clientAddress[1]} username: {user['data'].decode(PROTOCOL)}")

        else:
            message = receiveMessage(notifiedSocket)

            if message is False:
                print(f"Closed connewction {clients[notifiedSocket]['data'].decode(PROTOCOL)}")
                socketList.remove(notifiedSocket)
                del clients[notifiedSocket]
                continue

            user = clients[notifiedSocket]
            print(f"Received message from {user['data'].decode(PROTOCOL)}: {message['data'].decode(PROTOCOL)}")


            for client in clients:
                if client != notifiedSocket:
                    client.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notifiedSocket in exceptionSockets:
        socketList.remove(notifiedSocket)
        del clients[notifiedSocket]













