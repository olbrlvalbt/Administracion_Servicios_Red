from MonitorManager import MonitorManager
import rrdtool, time

def main():
	print("Examen")

	mm = MonitorManager()
	mm.addAgent( 'local' , 'localhost' , 'v2c' , 161 , 'comunidadASR' )
	time.sleep(1)

	while 1:
		print("1. Inicio")
		print("2. Agregar agente")
		print("3. Eliminar agente")
		print("4. Estado")

		opc = input()	

		if opc==1:
			print("1")
		if opc==2:
			id1 = raw_input("ID Agente: ")
			ip = raw_input("IP Agente: ")
			ver = raw_input("Version: ")
			puerto = input("Puerto: ")
			com = raw_input("Comunidad: ")
			mm.addAgent( id1 , ip , ver , puerto , com )
			
		if opc==3:
			print("3")
		if opc==4:
			print("4")	


main()

