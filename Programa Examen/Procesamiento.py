import rrdtool

def crearBases( name ):
	#1 BD Trafico de interfaz
	ret = rrdtool.create( name + "Trafico.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:InTraffic:COUNTER:600:U:U",
                     "DS:OutTraffic:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:20",
                     "RRA:AVERAGE:0.5:1:20")

	if ret:
		print (rrdtool.error())

	#2 BD Estadisticas IP
	ret = rrdtool.create( name + "Estadisticaip.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:InEstadisticaIPv4:COUNTER:600:U:U",
                     "DS:OutEstadisticaIPv4:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:20",
                     "RRA:AVERAGE:0.5:1:20")

	if ret:
		print (rrdtool.error())

	#3 BD Estadisticas ICPM
	ret = rrdtool.create( name + "Estadisticaicmp.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:InEstadisticaICMP:COUNTER:600:U:U",
                     "DS:OutEstadisticaICMP:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:20",
                     "RRA:AVERAGE:0.5:1:20")

	if ret:
		print (rrdtool.error())


	#4 BD Estadisticas SNMP
	ret = rrdtool.create( name + "Estadisticasnmp.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:InEstadisticaSNMP:COUNTER:600:U:U",
                     "DS:OutEstadisticaSNMP:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:20",
                     "RRA:AVERAGE:0.5:1:20")

	if ret:
		print (rrdtool.error())


	#5 BD Estadisticas TCP
	ret = rrdtool.create( name + "Estadisticastpc.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:InEstadisticaTCP:COUNTER:600:U:U",
                     "DS:OutEstadisticaTCP:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:20",
                     "RRA:AVERAGE:0.5:1:20")

	if ret:
		print (rrdtool.error())

	

def Ejecutar( comunidad , ip , name ):
	while 1:
	    
		#1 Trafico de interfaz
		total_input_traffic = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.2.2.1.10.1'))
	    	total_output_traffic = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.2.2.1.16.1'))

	    	valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
	    	rrdtool.update( name + 'Trafico.rrd', valor )
	    	rrdtool.dump( name + 'Trafico.rrd' , name + 'Trafico.xml' )

		#1 Grafica Trafico de interfaz
		ret = rrdtool.graph( name + "GraficoTrafico.png",
                     "--start",'1537495860',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=" + name + "Trafico.rrd:InTraffic:AVERAGE",
                     "DEF:outoctets=" + name + "Trafico.rrd:OutTraffic:AVERAGE",
                     "AREA:inoctets#00FF00:In traffic",
                     "LINE1:outoctets#0000FF:Out traffic\r")
	    



		#2 Estadisticas IP
		total_input_ipv4 = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.4.3.0'))
	    	total_output_ipv4 = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.4.10.0'))
	
		valor = "N:" + str(total_input_ipv4) + ':' + str(total_output_ipv4)
		rrdtool.update( name + 'Estadisticaip.rrd', valor )
	    	rrdtool.dump( name + 'Estadisticaip.rrd' , name + 'Estadisticaip.xml' )

		#2 Grafica Estadisticas IP
		ret = rrdtool.graph( name + "GraficoEstadisticaip.png",
                     "--start",'1537495860',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=" + name + "Estadisticaip.rrd:InEstadisticaIP:AVERAGE",
                     "DEF:outoctets=" + name + "Estadisticaip.rrd:OutEstadisticaIP:AVERAGE",
                     "AREA:inoctets#00FF00:In Estadistica IP",
                     "LINE1:outoctets#0000FF:Out Estadistica IP\r")


	

		#3 Estadisticas ICMP
		total_input_icmp = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.5.1.0'))
	    	total_output_icmp = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.5.14.0'))

		valor = "N:" + str(total_input_icmp) + ':' + str(total_output_icmp)
		rrdtool.update( name + 'Estadisticaicmp.rrd', valor )
	    	rrdtool.dump( name + 'Estadisticaicmp.rrd' , name + 'Estadisticaicmp.xml' )

		#3 Grafica Estadisticas ICMP
		ret = rrdtool.graph( name + "GraficoEstadisticaicmp.png",
                     "--start",'1537495860',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=" + name + "Estadisticaicmp.rrd:InEstadisticaICMP:AVERAGE",
                     "DEF:outoctets=" + name + "Estadisticaicmp.rrd:OutEstadisticaICMP:AVERAGE",
                     "AREA:inoctets#00FF00:In Estadistica ICMP",
                     "LINE1:outoctets#0000FF:Out Estadistica ICMP\r")




		#4 Estadisticas SNMP
		total_input_snmp = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.5.1.0'))
	    	total_output_snmp = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.5.14.0'))

		valor = "N:" + str(total_input_snmp) + ':' + str(total_output_snmp)
		rrdtool.update( name + 'Estadisticasnmp.rrd', valor )
	    	rrdtool.dump( name + 'Estadisticasnmp.rrd' , name + 'Estadisticasnmp.xml' )

		#4 Grafica Estadisticas SNMP
		ret = rrdtool.graph( name + "GraficoEstadisticasnmp.png",
                     "--start",'1537495860',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=" + name + "Estadisticasnmp.rrd:InEstadisticaSNMP:AVERAGE",
                     "DEF:outoctets=" + name + "Estadisticasnmp.rrd:OutEstadisticaSNMP:AVERAGE",
                     "AREA:inoctets#00FF00:In Estadistica SNMP",
                     "LINE1:outoctets#0000FF:Out Estadistica SNMP\r")




		#5 Estadisticas TCP
		total_input_tpc = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.6.10.0'))
	    	total_output_tpc = int(consultaSNMP( comunidad , ip ,'1.3.6.1.2.1.6.11.0'))

		valor = "N:" + str(total_input_tpc) + ':' + str(total_output_tpc)
		rrdtool.update( name + 'Estadisticastpc.rrd', valor )
	    	rrdtool.dump( name + 'Estadisticastpc.rrd' , name + 'Estadisticastpc.xml' )

		#5 Grafica Estadisticas TCP
		ret = rrdtool.graph( name + "GraficoEstadisticatcp.png",
                     "--start",'1537495860',
 #                    "--end","N",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=" + name + "Estadisticatcp.rrd:InEstadisticaTCP:AVERAGE",
                     "DEF:outoctets=" + name + "Estadisticatcp.rrd:OutEstadisticaTCP:AVERAGE",
                     "AREA:inoctets#00FF00:In Estadistica SNMP",
                     "LINE1:outoctets#0000FF:Out Estadistica SNMP\r")


		
		time.sleep(1)

	




