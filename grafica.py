import MySQLdb
import pygal

# CREAMOS LA LINEA PARA EL ACCESO A LA BBDD
db = MySQLdb.connect("localhost","usuario","password","database")
# CREAMOS C PARA EL USO DE CURSOR
c = db.cursor()
# PRIMERO LA FUNCION DE GRAFICA, EN ESTE CASO SIN INPUTS DEL EXTERIOR
def graph_data():
	# QUERY A LA BASE DE DATOS
	c.execute("SELECT hora, Entrante FROM altovideo")
	# VARIABLES DENTRO DE LA FUNCION
	datos = []
	valores = []
	# ACCION A REALIZAR PARA AÑADIR LOS DATOS DE COLUMNA EN LAS VARIABLES
	for row in c.fetchall():
		datos.append(row[0])
		valores.append(row[1])
	# CREACION PROPIA DE LA GRFICA
	line_chart = pygal.Line()
	line_chart.title = "alto video en Mbps"
	line_chart.x_labels = map(str, datos)
	line_chart.add('altovideo', valores)
	line_chart.render_to_file('prueba.svg')
graph_data()
c.close()
db.close()
