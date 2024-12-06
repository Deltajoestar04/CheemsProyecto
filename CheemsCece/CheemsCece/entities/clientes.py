from persistence.db import get_db_connection
from mysql.connector import Error

class Usuario:
    def __init__(self, id=None, nombre=None, password=None, id_ciudad=None):
        self.id = id 
        self.nombre = nombre
        self.password = password
        self.id_ciudad = id_ciudad
    
    @classmethod
    def get_all(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM usuario')
            return cursor.fetchall()
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_by_credentials(cls, nombre, password):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM usuario WHERE nombre = %s AND password = %s', (nombre, password))
            return cursor.fetchone()  
        except Error as e:
            return None  
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def save(cls, usuario):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO usuario (nombre, password, id_ciudad) VALUES (%s, %s, %s)',
                           (usuario.nombre, usuario.password, usuario.id_ciudad))
            connection.commit()
            return cursor.lastrowid  
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def update(cls, id, usuario):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute('UPDATE usuario SET nombre = %s, password = %s, id_ciudad = %s WHERE id = %s', 
                           (usuario.nombre, usuario.password, usuario.id_ciudad, id))
            connection.commit()
            return cursor.rowcount  
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_by_id(cls, id):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM usuario WHERE id = %s', (id,))
            return cursor.fetchone() 
        except Error as e:
            return None
        finally:
            cursor.close()
            connection.close()
