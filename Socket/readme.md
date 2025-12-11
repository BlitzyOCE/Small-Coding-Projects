# TCP Client-Server Chat Application

## What This Does


**server.py**: Creates a server that listens for connections, authenticates clients with a password, and allows chat communication.

**client.py**: Connects to the server, authenticates with a password, and enables the user to chat with the server.

![socket_illustration](images/1.gif)

## How to Run This

1. Run server: `python server.py`
2. Run client in another terminal: `python client.py`
3. Enter password: `secret123`
4. Start chatting
5. Type `end` to close connection

## How It Works

1. Server listens on port 9001
2. Client connects and sends password
3. Server checks password (grants/denies access)
4. If authenticated, both can exchange messages
5. Client types 'end' to disconnect

---

This is a coding practice project to get familiar with socket communication,
by Eric in Dec 2025.
