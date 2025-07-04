import socket

class ServidorChat:
	def __init__(self, ip='127.0.0.1', puerto=8090):
		self.ip = ip
		self.puerto = puerto
		self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def iniciar_chat(self):
		self.servidor.bind((self.ip, self.puerto))
		self.servidor.listen(1)
		print(f"Servidor escuchando en {self.ip}:{self.puerto}")
		conexion, direccion = self.servidor.accept()
		print("Conexión establecida con:", direccion)

		while True:
			datos = conexion.recv(1024).decode()
			if datos.lower() == "sayonara":#cambiar clave de salida
				print("El cliente ha cerrado la conexión.")
				break
			print("\033[92mEl cliente dice que:\033[0m")  # Mensaje en verde
			print("\033[92mCliente:", datos, "\033[0m")
			mensaje = input("Servidor: ")
			conexion.send(mensaje.encode())
			if mensaje.lower() == "sayonara": #cambiar clave de salida
				print("Servidor cerró la conexión.")
				break
		conexion.close()

if __name__ == "__main__":
	servidor = ServidorChat()
	servidor.iniciar_chat()