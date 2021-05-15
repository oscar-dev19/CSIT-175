import socket
HOST = '127.0.0.1'
PORT = 65432
INVALID_WORDS = ['DESTROY', 'REMOVE', 'DELETE']


              
              
def is_invalid_message(message):
    for word in INVALID_WORDS: 
        if word.lower() in message or word.upper() in message:
            return word.lower()
    return None
        
        

              
def authenticated(username):
    if username == 'master':
        return True
    else:
        return False    
          
          
def start_server(host=HOST,port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Connection from : {addr}, {port}')
            u_name = conn.recv(1024).decode()
            if authenticated(u_name):
                print('authenticated!')
                    conn.sendall('Enter a message -->'.encode())
                    message = conn.recv(1024).decode()
                    dangerous_word = is_invalid_message(message)
                    if dangerous_word:
                        conn.sendall(f'{dangerous_word} IS AN INVALID WORD!'.encode()) 
                    else:
                        conn.sendall(f'Received from Server: {message}'.encode())
            else:
                print('invalid')
                conn.sendall('INVALID USER NAME!\nENDING PROGRAM'.encode())
                conn.close()
                
                
                
                
                

    


                
def main():
    start_server()
        

if __name__ =='__main__':
    main()