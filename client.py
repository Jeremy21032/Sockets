import socket
import threading

username = input("Ingrese su nombre de usuario: ")
HOST = '25.10.177.48'
PORT = 2620

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def recieve_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "@username":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except KeyboardInterrupt:
            print('KeyboardInterrupt exception is caught')
            print("Ha ocurrido un error")
            client.close()
            break


def write_messages():
    while True:
        try:
            message = f"{username}: {input('')}"
            client.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            print('KeyboardInterrupt exception is caught')


receive_thread = threading.Thread(target=recieve_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
