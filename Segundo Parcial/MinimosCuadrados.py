import rrdtool, time, os, errno
from getSNMP import consultaSNMP
from os.path import basename

mcPath = os.getcwd() + "/rrd/minimosCuadrados/"

def EjecutarMc(rrdpath, varName, initialTime, finalTime, umbral):
        try:
                os.makedirs(os.path.dirname(mcPath))
        except OSError as exc:
                if exc.errno != errno.EEXIST:
                        print("Error de directorios: Minimos Cuadrados.")
                        raise

        name = basename(rrdpath)
        name = name[:(name.rfind('.'))]

        ret = rrdtool.graph(
                str(mcPath + name) + ".png",
                "--start", str(initialTime),
                "--end",str(finalTime),
                "--vertical-label=Carga",
                "--title=MINIMOS CUADRADOS",
                "--color", "ARROW#009900",
                '--vertical-label', "Carga",
                '--lower-limit', '0',
                '--upper-limit', '100',

                # ---CARGAS
                "DEF:carga=" + rrdpath + ":" + varName + ":AVERAGE",

                # ---GRAFICAR AREA
                "AREA:carga#00FF00:Load",

                # ---LINEA DE BASE
                #"HRULE:30#000000:Umbral 1",
                #"HRULE:35#00BB00:Umbral 2",
                "HRULE:" + str(umbral) + "#BB0000:Umbral",

                # ---ENTRADA DE CPU
                "LINE1:30",
                #"AREA:5#ff000022:stack",
                "VDEF:loadlast=carga,LAST",
                "VDEF:loadmin=carga,MINIMUM",
                "VDEF:loadavg=carga,AVERAGE",
                "VDEF:loadmax=carga,MAXIMUM",
                "COMMENT:          Now             Min               Avg                Max",
                "GPRINT:loadlast:%12.0lf%s",
                "GPRINT:loadmin:%10.0lf%s",
                "GPRINT:loadavg:%13.0lf%s",
                "GPRINT:loadmax:%13.0lf%s",

                # ---METODO DE MINIMOS CUADRADOS
                "VDEF:a=carga,LSLSLOPE",
                "VDEF:b=carga,LSLINT",
                'CDEF:avg2=carga,POP,a,COUNT,*,b,+',
                "LINE2:avg2#FFBB00",

                # ---Punto
                'CDEF:Cintersect=avg2,0,EQ,avg2,0,IF,' + str(umbral) + ',+,a,/,b,+,' + str(initialTime) + ',+',
                #'CDEF:Cintersect=avg2,'+str(umbral)+',EQ,avg2,0,IF',
                "VDEF:Pintersect=Cintersect,MAXIMUM",
                "COMMENT: Punto",
                "GPRINT:Pintersect:%8.0lf",
        )

        print("Archivo generado en " + mcPath)