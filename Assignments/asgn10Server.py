import socket
HOST = '127.0.0.1'
PORT = 65432
INVALID_WORDS = ['DESTROY', 'REMOVE', 'DELETE']


              
              
def contains_invalid_words(message):
    for word in INVALID_WORDS: 
        if word.lower() in message or word.upper() in message:
            return word.lower()
    return None
        
        

              
def authenticated(username):
    if username.lower() == 'master':
        return True
    else:
        return False    
          
          
def start_server(host=HOST,port=PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    conn, address = s.accept()
    print(f'Connection from: ({address},{port})')
    
    while True:
        data = conn.recv(1024)
        username = data.decode()
        print(f'from connected user: {username}')
        if authenticated(username):
            while True:
                conn.send('\nEnter a message -->'.encode())
                message = conn.recv(1024)
                print(f'from connected user: {message.decode()}')
                invalid_word = contains_invalid_words(message.decode())
                if invalid_word:
                    conn.send(f'Received from server: {invalid_word} IS AN INVALID WORD!'.encode())
                    continue
                else:
                    conn.send(f'Received from server: VALID: {message.decode()}'.encode())
                    continue
        else:
            conn.send('INVALID USER NAME!\nENDING PROGRAM'.encode())
            break
    conn.close()
            
                                
def main():
    start_server()
        

if __name__ =='__main__':
    main()