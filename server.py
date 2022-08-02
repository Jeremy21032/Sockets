import socket
import threading

HOST = '25.10.177.48'
PORT = 2620

# el primer argumento dice que vamos a  utilizar un socket tipo internet; el segundo significa que vamos a utilizar el protocolo TCP p
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"El servidor se está ejecutando en {HOST}:{PORT}")


# se crean dos listas para

clients = []  # se almacenan las conexiones de los usuarios
usernames = []  # almacenamos lo usernames de cada usuarios
# creación de mensaje para todos los clientes


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

# creación de funcion para manejar los mensajes de cada usuario


def handle_messages(client):
    while True:
        try:
            # la función va a leer como limite 1024 bytes y lo retornamos en un mensaje
            message = client.recv(1024)
            broadcast(message, client)
        except KeyboardInterrupt:
            print('KeyboardInterrupt exception is caught')
            index = clients.index(client)
            username = usernames.index[index]
            broadcast(
                f"\nChatBot: El usuario {username} se ha desconectado".encode('utf-8'),client)
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break
        except:
            # si ocurre un error, eliminamos el usuario de las listas y avisamos a los demás usuarios
            index = clients.index(client)
            username = usernames.index[index]
            broadcast(
                f"\nChatBot: El usuario {username} se ha desconectado".encode('utf-8'),client)
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break



def receive_connection():
    while True:
        try:
            client, address = server.accept()
            client.send("@username".encode('utf-8'))
            username = client.recv(1024).decode('utf-8')
            clients.append(client)
            usernames.append(username)
            print(
                f"El usuario {username} se ha conectado con la dirección {str(address)} ")
            message = f"ChatBot: El usuario {username} se unió a la conversación".encode(
                'utf8')
            broadcast(message, client)
            client.send("Conectado al servidor".encode('utf8'))

            thread = threading.Thread(target=handle_messages, args=(client,))
            thread.start()
        except KeyboardInterrupt:
            print('KeyboardInterrupt exception is caught')


receive_connection()
