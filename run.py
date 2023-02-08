from my_app import app
import pymysql

# Ejecuta la apliación.
# La instancia app de Flash se crea en el archivo __init__.py de my_app
app.config.from_pyfile("config.py")
app.run()

conn = pymysql.connect(
     host="localhost", port=3306, user="root",
     passwd="", db="pyalmacen"
 )

cursor = conn.cursor()
cursor.execute(
    "SELECT nombre, apellido FROM clientes"
)


for nombre, apellido in cursor.fetchall():
    print("{0} {1}".format(nombre, apellido))