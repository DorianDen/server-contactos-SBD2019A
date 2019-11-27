from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user='alumno', passwd='12345', database='Agenda')

cursor = bd.cursor()

@app.route('/agenda/', methods=["GET", "POST"])
def agenda():
    if request.method == "GET":
        contactos = []
        query = "SELECT * FROM contacto"
        cursor.execute(query)

        for contacto in cursor.fetchall():
            d = {
                'id': contacto[0],
                'nombre': contacto[1],
                'correo': contacto[2],
                'tel': contacto[3],
                'facebook': contacto[4],
                'instagram': contacto[5],
                'twitter': contacto[6],
                'avatar': contacto[7]
            }
            contactos.append(d)
            # print(contacto)
        print(contactos)
        return jsonify(contactos)
    else:
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto(nombre, correo, tel, facebook, instagram, twitter, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(query, (data['nombre'], data['correo'], data['telefono'], data['facebook'], data['instagram'], data['twitter'], data['avatar']))

        bd.commit()

        if cursor.rowcount:
            return jsonify({'data': 'ok'})
        else:
            return jsonify({'data': 'Error'})

app.run(debug=True)

