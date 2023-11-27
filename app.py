import base64
from cv2 import applyColorMap
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from cnx import DB_CONFIG
from app.operaciones import operaciones_bp
from app.ventas import ventas_bp
from app.cobranzas import cobranzas_bp

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Registra el Blueprint 'operaciones_bp' en tu aplicación
app.register_blueprint(operaciones_bp)
app.register_blueprint(ventas_bp)
app.register_blueprint(cobranzas_bp)

# Definición de filtro personalizado
def b64encode_filter(value):
    return base64.b64encode(value.encode('utf-8')).decode('utf-8')

# Debes agregar el filtro personalizado al entorno Jinja2 de tu aplicación Flask
app.jinja_env.filters['b64encode'] = b64encode_filter

def validar_acceso(user_name, user_password):
    try:
        # Configura la conexión a la base de datos
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        # Consulta para obtener el usuario y su rol
        query = "SELECT user_id, user_name, user_password, user_full_name, user_area FROM user WHERE user_name = %s"
        cursor.execute(query, (user_name,))
        result = cursor.fetchone()
        if result:
            # Verifica la contraseña
            if user_password == result[2]:
                # Devuelve el rol del usuario
                return result[0], result[1], result[2], result[3], result[4]
        return None  # Devuelve None si la autenticación falla
    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None
    finally:
        cursor.close()
        conn.close()

@app.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']

        result = validar_acceso(user_name, user_password)

        if result is not None:
            user_id, user_name, user_password, user_full_name, user_area = result

            session['user_id'] = user_id
            session['user_name'] = user_name
            session['user_password'] = user_password
            session['user_full_name'] = user_full_name
            session['user_area'] = user_area

            if user_area == 'OPERACIONES':
                return redirect(url_for('operaciones.support'))
            elif user_area == 'COMERCIAL':
                return redirect(url_for('ventas.sale'))
            elif user_area == 'COBRANZAS':
                return redirect(url_for('cobranzas.collections'))
            else:
                # Manejar otros roles aquí si es necesario
                pass

        else:
            render_template('login.html')

    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cerrarSesion')
def cerrarSesion():
    session.clear()
    return redirect(url_for('index'))

















@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
