import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print('[*] Listening on {}:{}'.format(bind_ip, bind_port))

def handle_client(csocket):
	request = csocket.recv(1024)
	print('[*] Received: {}'.format(request))
	csocket.send(b'ACK!')
	csocket.close()

while True:
	client, addr = server.accept()
	print('[*] Accepted connection from: {}:{}'.format(addr[0], addr[1]))

	handler = threading.Thread(target=handle_client, args=(client,))
	handler.start()
