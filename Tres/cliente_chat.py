import socket

class ClienteChat:
	def __init__(self, ip='127.0.0.1', puerto=8090):
		self.ip = ip
		self.puerto = puerto
		self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def iniciar_chat(self):
		self.cliente.connect((self.ip, self.puerto))
		while True:
			mensaje = input("Cliente: ")
			self.cliente.send(mensaje.encode())
			if mensaje.lower() == "sayonara":#cambiar clave de salida
				print("Cliente cerró la conexión.")
				break
			respuesta = self.cliente.recv(1024).decode()
			if respuesta.lower() == "sayonara":#cambiar clave de salida
				print("El servidor ha cerrado la conexión.")
				break
			print("\033[94mEl servidor dice que:\033[0m") #Agregar un mensaje de prefgijo automatico que dice quien es.
			print("\033[94mServidor:", respuesta, "\033[0m")
		self.cliente.close()

if __name__ == "__main__":
	cliente = ClienteChat()
	cliente.iniciar_chat()