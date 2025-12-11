import socket

server_password = "secret123"

# create a tcpip socket with ipv4 and tcp protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define server address and port
host = "127.0.0.1"
port = 9001

# bind socket to the host and port
s.bind((host, port))

# start listening for incoming connections
s.listen()

conn, addr = s.accept()
print(f'Connection received from {addr}')


# authentication
password_attempt = conn.recv(1024).decode()

if password_attempt != server_password:
    conn.send('Access denied - wrong password'.encode())
    conn.close
    print('Access denied - wrong password')
else:
    conn.send('Access granted'.encode())
    print('Client authenticated successfully')

    # chat function if successful authentication
    while True:
        msg = conn.recv(1024).decode()

        if msg.lower() == 'end':
            print("Client ended the connection")
            break

        print(f'Client: {msg}')

        reply = input("Enter message: ")

        conn.send(reply.encode())

conn.close()
print("Connection closed")



    

