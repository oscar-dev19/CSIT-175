import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with client_socket:
    client_socket.connect((HOST, PORT))
    username = input('What is your username? --> ')
    client_socket.sendall(username.encode())
    username_response = client_socket.recv(1024).decode()
    print(username_response)
    while True:
        message = input()
        if message.upper() == 'Q':
            break
        client_socket.sendall(message.encode())
        message_response = client_socket.recv(1024).decode()
        print(message_response)
    client_socket.close()
client_socket.close()
    
    
        
    
       
    


