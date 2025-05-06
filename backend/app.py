from flask import Flask, jsonify, request  # Asegúrate de importar `request`
from flask_cors import CORS
import mysql.connector
from config import db_config

app = Flask(__name__)
CORS(app)  # Habilita conexión con React (CORS)

@app.route('/')
def home():
    return jsonify({"mensaje": "API del Taller funcionando!"})

# Esta es la ruta para probar la conexión a la base de datos
@app.route("/probar-db")
def probar_db():
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM clientes;")
        cantidad = cursor.fetchone()[0]
        conexion.close()
        return jsonify({"mensaje": f"La base de datos está conectada. Hay {cantidad} clientes."})
    except Exception as e:
        return jsonify({"error": str(e)})

# Ruta para obtener todos los clientes
@app.route("/clientes", methods=["GET"])
def obtener_clientes():
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes;")
        clientes = cursor.fetchall()
        conexion.close()

        # Verificar que estamos obteniendo los datos correctamente
        print("Datos obtenidos de la base de datos:", clientes)  # Agrega esto para depurar

        lista_clientes = [
            {"id": cliente[0], "name": cliente[1], "telefono": cliente[2], "email": cliente[3], "direccion": cliente[4]}
            for cliente in clientes
        ]

        return jsonify(lista_clientes)
    except Exception as e:
        return jsonify({"error": str(e)})

# Ruta para agregar un nuevo cliente
@app.route("/clientes", methods=["POST"])
def agregar_cliente():
    try:
        # Obtener los datos del cliente desde el cuerpo de la solicitud
        datos = request.get_json()
        nombre = datos['nombre']
        telefono = datos['telefono']
        email = datos['email']
        direccion = datos['direccion']
        
        # Insertar los datos en la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO clientes (nombre, telefono, email, direccion) VALUES (%s, %s, %s, %s)",
                       (nombre, telefono, email, direccion))
        conexion.commit()
        conexion.close()
        
        return jsonify({"mensaje": "Cliente agregado exitosamente!"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/vehiculos", methods=["GET"])
def obtener_vehiculos():
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos;")
        vehiculos = cursor.fetchall()
        conexion.close()

        # Convertir los resultados a un formato JSON
        vehiculos_lista = []
        for vehiculo in vehiculos:
            vehiculos_lista.append({
                "id": vehiculo[0],
                "marca": vehiculo[1],
                "modelo": vehiculo[2],
                "patente": vehiculo[3],
                "anio": vehiculo[4],
                "cliente_id": vehiculo[5]
            })

        return jsonify(vehiculos_lista)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/vehiculos", methods=["POST"])
def agregar_vehiculo():
    try:
        # Obtener los datos del vehículo desde el cuerpo de la solicitud
        datos = request.get_json()
        marca = datos['marca']
        modelo = datos['modelo']
        patente = datos['patente']
        anio = datos['anio']
        cliente_id = datos['cliente_id']  # El ID del cliente asociado

        # Insertar los datos en la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO vehiculos (marca, modelo, patente, anio, cliente_id) VALUES (%s, %s, %s, %s, %s)",
                       (marca, modelo, patente, anio, cliente_id))
        conexion.commit()
        conexion.close()

        return jsonify({"mensaje": "Vehículo agregado exitosamente!"})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/vehiculos/<int:id>", methods=["PUT"])
def actualizar_vehiculo(id):
    try:
        # Obtener los datos del vehículo desde el cuerpo de la solicitud
        datos = request.get_json()
        marca = datos['marca']
        modelo = datos['modelo']
        patente = datos['patente']
        anio = datos['anio']

        # Actualizar el vehículo en la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("UPDATE vehiculos SET marca=%s, modelo=%s, patente=%s, anio=%s WHERE id=%s",
                       (marca, modelo, patente, anio, id))
        conexion.commit()
        conexion.close()

        return jsonify({"mensaje": "Vehículo actualizado exitosamente!"})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/vehiculos/<int:id>", methods=["DELETE"])
def eliminar_vehiculo(id):
    try:
        # Eliminar el vehículo de la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM vehiculos WHERE id=%s", (id,))
        conexion.commit()
        conexion.close()

        return jsonify({"mensaje": "Vehículo eliminado exitosamente!"})

    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route("/reparaciones", methods=["POST"])
def agregar_reparacion():
    try:
        datos = request.get_json()
        vehiculo_id = datos["vehiculo_id"]
        descripcion = datos["descripcion"]
        fecha = datos["fecha"]
        costo = datos["costo"]

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO reparaciones (vehiculo_id, descripcion, fecha, costo) VALUES (%s, %s, %s, %s)",
            (vehiculo_id, descripcion, fecha, costo)
        )
        conexion.commit()
        conexion.close()

        return jsonify({"mensaje": "Reparación registrada exitosamente!"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/reparaciones", methods=["GET"])
def obtener_reparaciones():
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reparaciones")
        reparaciones = cursor.fetchall()
        conexion.close()
        return jsonify(reparaciones)
    except Exception as e:
        return jsonify({"error": str(e)})






if __name__ == '__main__':
    app.run(debug=True)

