import os
import time


def openCmdStarServer(number):
    '''
    This method is used to open a Command Prompt and creates "number" servers
    :param number: represents the number of pieces, I set it for 1 server
    :return:
    '''
    for i in range(0, number):
        if i == 0:
            os.system(f"start cmd /k python {serverLocation}")
        else:
            break


def openCmdStartClient(number):
    '''
    This method is used to open a Command Prompt and creates "number" clients
    :param number: represents the number of pieces
    :return:
    '''
    for i in range(0, number):
        time.sleep(0.05)
        os.system((f"start cmd /k python {clientLocation}"))

def runXServersAndYClients(x, y):
    '''
    This is the final method that incorporates the other methods
    :param x: create x number of servers, I set it for 1 server
    :param y: create y number of clients
    :return:
    '''
    try:
        x, y = int(x), int(y)
        openCmdStarServer(x)
        time.sleep(5)
        openCmdStartClient(y)
    except:
        print("error: invalid integer!")


# exemple: use this "/", not this "\"
# serverLocation = 'C:/Users/Liviu/PycharmProjects/Nou/problema_3/PORT8000/serverPORT8000.py'
# clientLocation = 'C:/Users/Liviu/PycharmProjects/Nou/problema_3/PORT8000/clientPORT8000.py'

serverLocation = input("Enter the path to server location: ")
clientLocation = input("Enter the path to client location: ")
x = input("How many servers do you want to open?: ")
y = input("How many clients do you want to open?: ")

'''in this case you should open 1 server and more than 50 clients, after pressing the start button you have about 5 seconds to drag the first window to a safe and visible place,
the first window is the server window, before mixing with the other +50 clients that will run at the same time.'''

runXServersAndYClients(x, y)

