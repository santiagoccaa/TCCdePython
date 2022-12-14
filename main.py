from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL
from database import database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#--------------FORMULARIOS

@app.route('/form')
def form():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM formulario1")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('formulario1.html', data=insertObject)

#-------------GUARDAR DATOS----------------

@app.route('/user', methods=['POST'])
def objeto():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    marca = request.form['marca']

    if nombre and cantidad and marca:
        cursor = database.cursor()
        sql = "INSERT INTO formulario1 (nombre, cantidad, marca) VALUES (%s, %s, %s)"
        data = (nombre, cantidad, marca)
        cursor.execute(sql, data)
        database.commit()
    return redirect(url_for('form'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = database.cursor()
    sql = "DELETE FROM formulario1 WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    database.commit()
    return redirect(url_for('form'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    marca = request.form['marca']

    if nombre and cantidad and marca:
        cursor = database.cursor()
        sql = "UPDATE formulario1 SET nombre = %s, cantidad = %s, marca = %s WHERE id = %s"
        data = (nombre, cantidad, marca, id)
        cursor.execute(sql, data)
        database.commit()
    return redirect(url_for('form'))

#--------#FORMULARIO SALA 2-----------------------------------------------------


@app.route('/sala')
def sala():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM formulario2")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('formulario2.html', data=insertObject)

#-------------GUARDAR DATOS----------------

@app.route('/user2', methods=['POST'])
def objeto1():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    marca = request.form['marca']

    if nombre and cantidad and marca:
        cursor = database.cursor()
        sql = "INSERT INTO formulario2 (nombre, cantidad, marca) VALUES (%s, %s, %s)"
        data = (nombre, cantidad, marca)
        cursor.execute(sql, data)
        database.commit()
    return redirect(url_for('sala'))

@app.route('/delete1/<string:id>')
def delete1(id):
    cursor = database.cursor()
    sql = "DELETE FROM formulario2 WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    database.commit()
    return redirect(url_for('sala'))

@app.route('/edit1/<string:id>', methods=['POST'])
def edit1(id):
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    marca = request.form['marca']

    if nombre and cantidad and marca:
        cursor = database.cursor()
        sql = "UPDATE formulario2 SET nombre = %s, cantidad = %s, marca = %s WHERE id = %s"
        data = (nombre, cantidad, marca, id)
        cursor.execute(sql, data)
        database.commit()
    return redirect(url_for('sala'))


#--------------------FORMULARIO 3------------------------

@app.route('/sala3')
def sala3():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM formulario3")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('formulario3.html', data=insertObject)

#-------------GUARDAR DATOS----------------

@app.route('/user3', methods=['POST'])
def objeto2():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    marca = request.form['marca']

    if nombre and cantidad and marca:
        cursor = database.cursor()
        sql = "INSERT INTO formulario3 (nombre, cantidad, marca) VALUES (%s, %s, %s)"
        data = (nombre, cantidad, marca)
        cursor.execute(sql, data)
        database.commit()
    return redirect(url_for('sala3'))

@app.route('/delete2/<string:id>')
def delete2(id):
    cursor = database.cursor()
    sql = "DELETE FROM formulario3 WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    database.commit()
    return redirect(url_for('sala3'))

@app.route('/edit2/<string:id>', methods=['POST'])
def edit2(id):
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    marca = request.form['marca']

    if nombre and cantidad and marca:
        cursor = database.cursor()
        sql = "UPDATE formulario3 SET nombre = %s, cantidad = %s, marca = %s WHERE id = %s"
        data = (nombre, cantidad, marca, id)
        cursor.execute(sql, data)
        database.commit()
    return redirect(url_for('sala3'))    


if __name__ == '__main__':
    app.run(debug=True, port=8000)