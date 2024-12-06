from flask import Flask, request, jsonify, render_template, redirect, url_for
from entities.ciudad import Ciudad
from persistence.db import get_db_connection
from entities.clientes import Usuario
from entities.paquetes import Paquete
import bcrypt  # Librería para manejo de contraseñas seguras
from random import randint  # Para generar códigos aleatorios

app = Flask(__name__)
  
# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# --------- CIUDADES ---------

@app.route('/ciudades')
def ciudades():
    ciudades = Ciudad.get_all()
    return render_template('ciudades.html', ciudades=ciudades)

@app.route('/page')
def page():
    return render_template('page.html')


@app.route('/ciudad-registro', methods=['GET'])
def ciudad_registro():
    return render_template('ciudad.html')

@app.route('/ciudad', methods=['GET'])
def get_ciudades():
    ciudades = Ciudad.get_all()
    return jsonify(ciudades), 200

@app.route('/ciudad', methods=['POST'])
def save_ciudad():
    data = request.json
    ciudad = Ciudad(nombre=data['nombre'], codigo=data['codigo'])
    id = Ciudad.save(ciudad)
    return jsonify({'id': id}), 201

@app.route('/ciudad/<int:id>', methods=['PUT'])
def update_ciudad(id):
    data = request.json
    ciudad = Ciudad(nombre=data['nombre'], codigo=data['codigo'])
    result = Ciudad.update(id, ciudad)
    if result == 0:
        return jsonify({'error': 'El registro de ciudad no existe'}), 404
    return jsonify({'id': id}), 201

# --------- USUARIOS ---------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        password = request.form.get('password')

        if not nombre or not password:
            return render_template('login.html', error='Campos obligatorios')

        usuario = Usuario.get_by_credentials(nombre)
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
            return redirect(url_for('central'))
        return render_template('login.html', error='Usuario o contraseña incorrectos')

    return render_template('login.html')

@app.route('/central')
def central():
    return render_template('central.html')

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    nombre = data.get('nombre')
    contrasenia = data.get('contrasenia')
    ciudad = data.get('ciudad')

    if not nombre or not contrasenia or not ciudad:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    hashed_password = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())
    usuario = Usuario(nombre=nombre, password=hashed_password.decode('utf-8'), id_ciudad=ciudad)
    try:
        usuario_id = Usuario.save(usuario)
        return jsonify({'message': 'Usuario registrado correctamente', 'id': usuario_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/inicio', methods=['POST'])
def inicio():
    data = request.get_json()
    nombre = data.get('nombre')
    contrasenia = data.get('contrasenia')

    if not nombre or not contrasenia:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    usuario = Usuario.get_by_credentials(nombre)
    if usuario and bcrypt.checkpw(contrasenia.encode('utf-8'), usuario['password'].encode('utf-8')):
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    return jsonify({'error': 'Nombre o contraseña incorrectos'}), 401

# --------- PAQUETES ---------

@app.route('/paquetes')
def paquetes():
    paquetes = Paquete.get_all()
    return render_template('paquetes.html', paquetes=paquetes)

@app.route('/paquete-registro', methods=['GET'])
def paquete_registro():
    return render_template('newpaquete.html')  # Asegúrate de usar este template

@app.route('/paquete', methods=['GET'])
def get_paquetes():
    paquetes = Paquete.get_all()
    return jsonify(paquetes), 200

@app.route('/paquete', methods=['POST'])
def save_paquete():
    """
    Guarda un nuevo paquete con un código generado automáticamente.
    """
    try:
        data = request.json
        # Generar un código único aleatorio para el paquete
        codigo_paquete = f"PKG-{randint(10000, 99999)}"

        paquete = Paquete(
            id_cliente=data['id_cliente'],
            fecha_envio=data['fecha_envio'],
            fecha_llegada=data.get('fecha_llegada', None),
            tamano=data['tamano'],
            codigo_paquete=codigo_paquete,
            estado=data['estado']
        )
        id = Paquete.save(paquete)
        return jsonify({'id': id, 'codigo_paquete': codigo_paquete}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/paquete/<int:id>', methods=['PUT'])
def update_paquete(id):
    data = request.json
    paquete = Paquete(
        id_cliente=data['id_cliente'],
        fecha_envio=data['fecha_envio'],
        fecha_llegada=data['fecha_llegada'],
        tamano=data['tamano'],
        codigo_paquete=data['codigo_paquete'],
        estado=data['estado']
    )
    result = Paquete.update(id, paquete)
    if result == 0:
        return jsonify({'error': 'El paquete no existe'}), 404
    return jsonify({'id': id}), 200

@app.route('/paquete/<int:id>', methods=['DELETE'])
def delete_paquete(id):
    result = Paquete.delete(id)
    if result == 0:
        return jsonify({'error': 'El paquete no existe'}), 404
    return jsonify({'message': 'Paquete eliminado exitosamente'}), 200

@app.route('/verificar_codigo', methods=['POST'])
def verificar_codigo():
    try:
        data = request.get_json()
        codigo_paquete = data.get('codigo_paquete')

        if not codigo_paquete:
            return jsonify({'existe': False, 'mensaje': 'Código de rastreo no proporcionado'}), 400

        paquete = Paquete.get_by_codigo(codigo_paquete)
        if paquete:
            return jsonify({'existe': True})
        return jsonify({'existe': False})
    except Exception as e:
        return jsonify({'existe': False, 'mensaje': str(e)}), 500

# --------- MAIN ---------

if __name__ == '__main__':
    app.run(debug=True)
