import socket

# create a tcpip socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define server address and port
host = "127.0.0.1"
port = 9001

# establish the connection
s.connect((host, port))
print("Connected to server")

# authentication
password = input("Enter password: ")

s.send(password.encode())
response = s.recv(1024).decode()

if response == 'Access denied - wrong password':
    print(response)
    s.close
else:
    print(response)

    # chat function
    while True:
        msg = input("Enter message here to send, or type end to close chat: ")

        s.send(msg.encode())

        if msg.lower() == 'end':
            print("Connection ended")
            break

        reply = s.recv(1024).decode()

        print(f'Server: {reply}')

s.close()
print("Connection closed")
