import socket

"""     '127.0.0.1' | "localhost" | '' - param for local settings, access from WAN will be denied
        socket.gethostname() - param for WAN, access from WAN will be granted
"""
SERVER_ADDRESS = socket.gethostname()

SERVER_PORT = 53        # standart  DNS port
SERVER_HOST_PORT = (socket.gethostname(), SERVER_PORT)
CONN_TYPE = socket.SOCK_DGRAM    #socket.SOCK_DGRAM(UDP protocol), socket.SOCK_STREAM(TCP protocol)

def init_server():
    try:
        sock = socket.socket(CONN_TYPE)         # create socket
        sock.bind(SERVER_HOST_PORT)                             # connect created socket with port
        sock.listen()
        print('Socket: created, bond and listening')
        print('Server status: RUN')
    except:
        print('Server init: FAIL')

    sock.accept()

init_server()