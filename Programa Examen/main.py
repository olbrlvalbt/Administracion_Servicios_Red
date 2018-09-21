from MonitorManager import MonitorManager
import rrdtool, time

mm = MonitorManager()
mm.addAgent('local', 'localhost', 'v2c', 161, 'comunidadASR')

def main():
	print("Examen")
	menu()


def menu():
	while 1:
		print
		print("1. Inicio")
		print("2. Agregar Agente")
		print("3. Eliminar Agente")
		print("4. Estado agente")
		print("5. Salir")
		opc = input("Elige una opcion: ")
		if opc == 1:
			mm.showAll()

		if opc == 2:
			idAgente = raw_input("IdAgente: ")
			hostname = raw_input("Hostname: ")
			version = raw_input("Version: ")
			port = int(raw_input("Port: "))
			comunity = raw_input("Comunity: ")
			if mm.addAgent(idAgente, hostname, version, port, comunity):
				print(idAgente + " registrado.")
			else:
				print("Ya existe el idAgente.")

		if opc == 3:
			idAgente = raw_input("IdAgente: ")
			if mm.removeAgent(idAgente):
				print(idAgente + " eliminado.")
			else:
				print("No se encontro el idAgente.")

		if opc == 4:
			idAgente = raw_input("IdAgente: ")
			if not mm.consulta(idAgente):
				print("No se encontro el idAgente.")
			
		if opc == 5:
			print("Cerrando monitores.")
			break;

main()
