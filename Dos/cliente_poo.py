import socket



class Cliente:
	
    
	def __init__(self, ip='127.0.0.1', puerto=8090):
		self.ip = ip
		self.puerto = puerto
		self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def comunicarse(self):
		self.cliente.connect((self.ip, self.puerto))
		mensaje = input("Escribe un mensaje para el servidor: ")
		self.cliente.send(mensaje.encode())
		respuesta = self.cliente.recv(1024).decode()
		print("Respuesta del servidor:", respuesta)
		self.cliente.close()
    
	def Mensaje_final(self):
		mensajef = "Gracias por comunicarte, hasta luego!"
		self.cliente.send(mensajef.encode()) #mensaje final de despedida al recibir respuesta

if __name__ == "__main__":
	cliente = Cliente()
	cliente.comunicarse()
	cliente.Mensaje_final()