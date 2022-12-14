import mysql.connector


conexion= mysql.connector.connect(
	host='localhost',
	user='root',
	password=''
)

cursor=conexion.cursor()

cursor.execute("CREATE DATABASE formulario")

conexion= mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	db='formm'
)

cursor.execute("CREATE TABLE formulario1 (id AUTO_INCREMENT PRYMARY KEY, nombre VARCHAR(50), cantidad VARCHAR(50), MARCA varchar(50))")
