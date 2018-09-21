from MonitorManager import MonitorManager
import rrdtool, time

def main():
	print("Examen")

	mm = MonitorManager()

	time.sleep(5)

	mm.addAgent('local', 'localhost', 'v2c', 161, 'comunidadASR')



main()

