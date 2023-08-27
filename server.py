import socket
import threading
 
# Connection Data
host = '192.168.130.86'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
 
 
# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        
        if (bytes("idiot", 'utf-8') in message):
            client.send(bytes("Server: Refine Language", 'utf-8'))  
        elif (bytes("stupid", 'utf-8') in message):
            client.send(bytes("Server: Refine Language", 'utf-8'))   
        elif (bytes("dumb", 'utf-8') in message):
            client.send(bytes("Server: Refine Language", 'utf-8'))      
        elif (bytes("hi", 'utf-8') in message):
            client.send(bytes("Server: Welcome Buddy", 'utf-8'))  
            client.send(message)  
        elif (bytes("bye", 'utf-8') in message):
            client.send(bytes("Server: Have a great day!!", 'utf-8'))  
            client.send(message) 
        elif (bytes("sentiment", 'utf-8') in message):
            client.send(bytes("Server: Chillax", 'utf-8'))    
            client.send(message)      
        elif (bytes("cool", 'utf-8') in message):
            client.send(bytes("Server: Rock!!", 'utf-8'))    
            client.send(message)     
        elif (bytes("bloody", 'utf-8') in message):
            client.send("!")   
        elif (bytes("donkey", 'utf-8') in message):
            client.send("!")         
        else:              
            client.send(message)
 
 
# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break 

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()