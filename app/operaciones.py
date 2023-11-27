import datetime
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session
from functools import wraps
import mysql.connector
import openpyxl
from app.models import clientes_imp, clientes_imp_filtrados, create_new_implementation, create_newAtention, detail_MonthlySupport, detail_Support, detail_contact, detail_contactS, detail_follow_up, detail_follow_update, detail_followU, list_follow_up, list_monthly_support, list_trains, list_users, new_company, new_train, obtener_info_clientes, obtener_info_clientes_contrato, obtener_info_clientes_filtrados, obtener_new_clientes, obtener_new_clientes_filtrados, register_follow_contact, register_support_contact
from cnx import DB_CONFIG
from datetime import datetime

operaciones_bp = Blueprint('operaciones', __name__)


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'user_name' in session and 'user_password' in session:
            return route_function(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

@operaciones_bp.route('/buscar_contrato', methods=['GET'])
def buscar_contrato():
    ruc = request.args.get('ruc', '')
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT contract_number FROM company WHERE ruc = %s", (ruc,))
        resultado = cursor.fetchone()

        if resultado:
            contrato_encontrado = resultado[0]
        else:
            contrato_encontrado = ''

        return contrato_encontrado

    except Exception as e:
        print(f"Error al buscar contrato: {e}")
        return jsonify({'error': 'Error al buscar contrato'}), 500

    finally:
        cursor.close()
        conn.close()

@operaciones_bp.route('/verificar_ruc', methods=['GET'])
def verificar_ruc():
    ruc = request.args.get('ruc')

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Ejecuta la consulta SQL para verificar si el RUC existe en la tabla new_client.
        cursor.execute(
            "SELECT COUNT(*) AS ruc_exists FROM implementation WHERE ruc = %s", (ruc,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result[0] > 0:
            return jsonify({'exists': True})
        else:
            return jsonify({'exists': False})
    except Exception as e:
        return jsonify({'error': str(e)})


@operaciones_bp.route('/validar_client', methods=['GET'])
def validar_client():
    ruc = request.args.get('ruc')

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Ejecuta la consulta SQL para verificar si el RUC existe en la tabla new_client.
        cursor.execute(
            "SELECT COUNT(*) AS ruc_exists FROM new_client WHERE ruc = %s", (ruc,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result[0] > 0:
            return jsonify({'exists': True})
        else:
            return jsonify({'exists': False})
    except Exception as e:
        return jsonify({'error': str(e)})


@operaciones_bp.route('/newImplmentation', methods=['GET', 'POST'])
@login_required
def newImplmentation():
    user_id = session.get('user_id')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        contract_number = request.form.get('contract_number')
        if 'pass_sun_boolean' in request.form:
            pass_sun_boolean = True
            pass_sun = request.form.get('pass_sun')
            pass_pass_sun = request.form.get('pass_pass_sun')
        else:
            pass_sun_boolean = False
            pass_sun = ""
            pass_pass_sun = ""

        comercial_name = request.form.get('comercial_name')
        comercial_address = request.form.get('comercial_address')
        comercial_phone = request.form.get('comercial_phone')
        comercial_email = request.form.get('comercial_email')
        taxes = request.form.get('taxes')
        secundary_user = request.form.get('secundary_user')
        pass_secundary_user = request.form.get('pass_secundary_user')
        url_cd = request.form.get('url_cd')
        pass_cd = request.form.get('pass_cd')
        expiration_cd = request.form.get('expiration_cd')
        gr_pass = request.form.get('gr_pass')
        gr_id = request.form.get('gr_id')

        create_new_implementation(ruc, user_id, contract_number, pass_sun_boolean, pass_sun, pass_pass_sun, comercial_name, comercial_address,
                                  comercial_phone, comercial_email, taxes, secundary_user, pass_secundary_user, url_cd, pass_cd, expiration_cd, gr_pass, gr_id)

        return redirect(url_for('operaciones.list_implementation')) 


@operaciones_bp.route('/support', methods=['GET', 'POST'])
@login_required
def support():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        lista_clientes = obtener_info_clientes_filtrados(ruc)
    else:
        lista_clientes = obtener_info_clientes()

    return render_template('operaciones/support.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, lista_clientes=lista_clientes)


@operaciones_bp.route('/searchSupport', methods=['GET', 'POST'])
@login_required
def searchSupport():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    if request.method == 'POST':
        contract_number = request.form.get('contract_number')
        cliente = obtener_info_clientes_contrato(contract_number)
    else:
        cliente = [""]

    return render_template('operaciones/searchSupport.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, cliente=cliente)


@operaciones_bp.route('/implementation')
@login_required
def implementation():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    client = request.args.get('cliente')

    return render_template('operaciones/implementation.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, client=client)


@operaciones_bp.route('/list_implementation', methods=['GET', 'POST'])
@login_required
def list_implementation():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        lista_clientes = clientes_imp_filtrados(ruc)
    else:
        lista_clientes = clientes_imp()

    return render_template('operaciones/list_implementation.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, lista_clientes=lista_clientes)


@operaciones_bp.route('/newCompany', methods=['GET', 'POST'])
@login_required
def newCompany():
    user_id = session.get('user_id')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        contract_number = request.form.get('contract_number')
        support_email = request.form.get('support_email')
        support_pass = request.form.get('support_pass')

        new_company(user_id, ruc, contract_number, support_email, support_pass)

        return redirect(url_for('operaciones.list_implementation'))


@operaciones_bp.route('/follow_up', methods=['GET', 'POST'])
@login_required
def follow_up():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        lista_clientes = obtener_new_clientes_filtrados(ruc)
        users = list_users()
    else:
        lista_clientes = obtener_new_clientes()
        users = list_users()

    return render_template('operaciones/follow_up.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, lista_clientes=lista_clientes, users=users)


@operaciones_bp.route('/list_train', methods=['GET', 'POST'])
@login_required
def list_train():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    list_train = list_trains()
    users = list_users()

    return render_template('operaciones/list_train.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, list_train=list_train, users=users)


@operaciones_bp.route('/inactive_tracking', methods=['GET', 'POST'])
@login_required
def inactive_tracking():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        list_follow = obtener_new_clientes()
    else:
        list_follow = list_follow_up()
        users = list_users()

    return render_template('operaciones/inactive_tracking.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, list_follow=list_follow, users=users)


@operaciones_bp.route('/monthly_support', methods=['GET', 'POST'])
@login_required
def monthly_support():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    list = list_monthly_support()
    users = list_users()

    return render_template('operaciones/monthly_support.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, list=list, users=users)


@operaciones_bp.route('/newAtention', methods=['GET', 'POST'])
@login_required
def newAtention():
    user_id = session.get('user_id')

    if request.method == 'POST':
        register_id = request.form.get('register_id')
        ruc_support = request.form.get('ruc_support')
        contract_number = request.form.get('contract_number')
        problem = request.form.get('problem')
        module = request.form.get('module')

    create_newAtention(register_id, ruc_support,
                       contract_number, user_id, problem, module)

    return redirect(url_for('operaciones.detail_MonthlyS', register_id=register_id))


@operaciones_bp.route('/detail_followUp', methods=['GET', 'POST'])
@login_required
def detail_followUp():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    id_follow = request.args.get('id_follow')
    details = detail_follow_up(id_follow)

    return render_template('operaciones/detail_follow_up.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, details=details, id_follow=id_follow)


@operaciones_bp.route('/detail_MonthlyS', methods=['GET', 'POST'])
@login_required
def detail_MonthlyS():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    register_id = request.args.get('register_id')
    details = detail_MonthlySupport(register_id)

    return render_template('operaciones/detail_MonthlyS.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, details=details, register_id=register_id)


@operaciones_bp.route('/detail_follow', methods=['GET', 'POST'])
@login_required
def detail_follow():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    id_details = request.args.get('id_details')
    detail = detail_followU(id_details)
    contact = detail_contact(id_details)

    return render_template('operaciones/detail_followUp.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, detail=detail, contact=contact, id_details=id_details)


@operaciones_bp.route('/detail_support', methods=['GET', 'POST'])
@login_required
def detail_support():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    id_details = request.args.get('id_details')
    detail = detail_Support(id_details)
    contact = detail_contactS(id_details)

    return render_template('operaciones/detail_support.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, detail=detail, contact=contact, id_details=id_details)


@operaciones_bp.route('/endTracking', methods=['GET', 'POST'])
@login_required
def endTracking():

    if request.method == 'POST':
        id_follow = request.form.get('id_follow_A')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE follow_up SET status = 'FINALIZADO' WHERE follow_up_id = %s", [id_follow])
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('operaciones.inactive_tracking'))


@operaciones_bp.route('/endMonthlySupport', methods=['GET', 'POST'])
@login_required
def endMonthlySupport():

    if request.method == 'POST':
        monthlySupport_id = request.form.get('monthlySupport_id')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE monthly_support SET status = 'FINALIZADO' WHERE monthlySupport_id = %s", [monthlySupport_id])
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('operaciones.monthly_support'))

@operaciones_bp.route('/newRegister', methods=['GET', 'POST'])
@login_required
def newRegister():

    monthly_mm = datetime.datetime.now().strftime('%B')
    year_yy = datetime.datetime.now().strftime('%Y')

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Verifica si ya existe un registro para el mes y año actuales
    query_existencia = "SELECT EXISTS(SELECT 1 FROM monthly_support WHERE monthly_mm = %s AND year_yy = %s)"
    cursor.execute(query_existencia, (monthly_mm, year_yy))
    existe_registro = cursor.fetchone()[0]

    if existe_registro:
        return redirect(url_for('operaciones.monthly_support'))
    else:
        # Inserta un nuevo registro
        query_insercion = "INSERT INTO monthly_support (monthly_mm, year_yy,status) VALUES (%s, %s,'EN PROCESO')"
        cursor.execute(query_insercion, (monthly_mm, year_yy))
        conn.commit()
        return redirect(url_for('operaciones.monthly_support'))

    



@operaciones_bp.route('/endDetailSupport', methods=['GET', 'POST'])
@login_required
def endDetailSupport():

    if request.method == 'POST':
        detail_monthly_S = request.form.get('detail_monthly_S')
        register_id = request.form.get('register_id')
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE detail_monthly_support SET status_case = 'FINALIZADO', end_time =%s WHERE detail_monthly_id = %s", [current_timestamp, detail_monthly_S])
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('operaciones.detail_MonthlyS', register_id=register_id))


@operaciones_bp.route('/detail_followUp_active', methods=['GET', 'POST'])
@login_required
def detail_follow_active():

    if request.method == 'POST':
        id_follow = request.form.get('id_follow_A')
        ruc = request.form.get('ruc_A')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE detail_follow_up SET final_estate = 'ACTIVO' WHERE ruc_follow_up = %s AND follow_up_id = %s", [ruc, id_follow])
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('operaciones.detail_followUp', id_follow=id_follow))


@operaciones_bp.route('/detail_followUp_contact', methods=['GET', 'POST'])
@login_required
def detail_follow_contact():

    if request.method == 'POST':

        id_follow = request.form.get('id_follow_C')
        detail_id = request.form.get('detail_id')
        type_contact = request.form.get('type_contact')
        comment_contact = request.form.get('comment_contact')

        register_follow_contact(detail_id, type_contact, comment_contact)

    return redirect(url_for('operaciones.detail_followUp', id_follow=id_follow))


@operaciones_bp.route('/detail_support_contact', methods=['GET', 'POST'])
@login_required
def detail_support_contact():

    if request.method == 'POST':

        register_id = request.form.get('register_id')
        detail_id = request.form.get('detail_id')
        type_contact = request.form.get('type_contact')
        comment_contact = request.form.get('comment_contact')

        register_support_contact(detail_id, type_contact, comment_contact)

    return redirect(url_for('operaciones.detail_MonthlyS', register_id=register_id))


@operaciones_bp.route('/detail_followUp_edit', methods=['GET', 'POST'])
@login_required
def detail_follow_edit():

    if request.method == 'POST':
        id_follow = request.form.get('id_follow_E')
        ruc_E = request.form.get('ruc_E')
        state_follow_up = request.form.get('state_follow_up')
        reason_follow_up = request.form.get('reason_follow_up')
        detail_follow_up = request.form.get('detail_follow_up')

        detail_follow_update(id_follow, ruc_E, state_follow_up, reason_follow_up,
                             detail_follow_up)

    return redirect(url_for('operaciones.detail_followUp', id_follow=id_follow))


@operaciones_bp.route('/detail_support_comment', methods=['GET', 'POST'])
@login_required
def detail_support_comment():

    if request.method == 'POST':
        register_id = request.form.get('register_id')
        detail_monthly = request.form.get('detail_monthly')
        commentry = request.form.get('commentry')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE detail_monthly_support SET commentry = %s WHERE detail_monthly_id = %s", [commentry, detail_monthly])
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('operaciones.detail_MonthlyS', register_id=register_id))


@operaciones_bp.route('/detail_support_derived', methods=['GET', 'POST'])
@login_required
def detail_support_derived():

    if request.method == 'POST':
        register_id = request.form.get('register_id')
        detail_monthly_id = request.form.get('detail_monthly_id')
        ticket = request.form.get('ticket')

        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE detail_monthly_support SET status_case = 'DERIVADO', derived = True , ticket = %s, time_derivative =%s WHERE detail_monthly_id = %s", [ticket, current_timestamp, detail_monthly_id])
        conn.commit()
        cursor.close()
        conn.close()

    return redirect(url_for('operaciones.detail_MonthlyS', register_id=register_id))


@operaciones_bp.route('/newTrain', methods=['GET', 'POST'])
@login_required
def newTrain():
    user_id = session.get('user_id')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        contract_number = request.form.get('contract_number')
        url_train = request.form.get('url_train')
        date_train = request.form.get('date_train')
        hour_train = request.form.get('hour_train')
        user_id_resp = request.form.get('user_id_resp')

        new_train(user_id, user_id_resp, ruc, contract_number,
                  url_train, date_train, hour_train)

    return redirect(url_for('operaciones.list_train'))


@operaciones_bp.route('/newFirstTrain', methods=['GET', 'POST'])
@login_required
def newFirstTrain():
    user_id = session.get('user_id')

    if request.method == 'POST':
        ruc = request.form.get('ruc')
        contract_number = request.form.get('contract_number')
        url_train = request.form.get('url_train')
        date_train = request.form.get('date_train')
        hour_train = request.form.get('hour_train')
        user_id_resp = request.form.get('user_id_resp')

        new_train(user_id, user_id_resp, ruc, contract_number,
                  url_train, date_train, hour_train)

    return redirect(url_for('operaciones.follow_up'))


@operaciones_bp.route('/acceptTrain', methods=['GET', 'POST'])
@login_required
def acceptTrain():
    if request.method == 'POST':
        ruc = request.form.get('ruc')
        train_id = request.form.get('train_id')
        activo = request.form.get('activo')
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        if activo == 'SI':
            cursor.execute(
                "SELECT * FROM company WHERE (ruc = %s AND status_train = 'AGENDADA') OR (ruc = %s AND status_train = 'NO REALIZADA') ", [ruc,ruc])
            results = cursor.fetchall()

            if len(results) == 1:
                cursor.execute(
                    "UPDATE company SET status_train = 'REALIZADA' WHERE ruc = %s", [ruc])

            cursor.execute(
                "UPDATE train SET status_train = 'REALIZADA' WHERE train_id = %s", [train_id])
            conn.commit()
            conn.close()

        if activo == 'NO':
            cursor.execute(
                "SELECT * FROM company WHERE ruc = %s AND status_train = 'AGENDADA' ", [ruc])
            results = cursor.fetchall()

            if len(results) == 1:
                cursor.execute(
                    "UPDATE company SET status_train = 'NO REALIZADA' WHERE ruc = %s", [ruc])

            cursor.execute(
            "UPDATE train SET status_train = 'NO REALIZADA' WHERE train_id = %s", [train_id])
            conn.commit()
            conn.close()

    return redirect(url_for('operaciones.list_train'))


@operaciones_bp.route('/activeCompany', methods=['GET', 'POST'])
@login_required
def activeCompany():
    if request.method == 'POST':
        ruc = request.form.get('ruc_C')
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE company SET status_comp = 'ACTIVO' WHERE ruc = %s", [ruc])

        conn.commit()
        conn.close()

    return redirect(url_for('operaciones.follow_up'))


@operaciones_bp.route('/upload_inactive_tracking', methods=['POST'])
@login_required
def upload_inactive_tracking():

    user_id = session.get('user_id')

    if 'excelFile' not in request.files:
        return redirect(request.url)
    excel_file = request.files['excelFile']

    if excel_file.filename == '':
        return redirect(request.url)

    # Leer el archivo de Excel
    try:
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active
        columna_ruc = sheet['A']
    except Exception as e:
        return f"Error al leer el archivo de Excel: {str(e)}"

    # Insertar en la tabla follow_up
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO follow_up (user_id,status) VALUES (%s,'EN PROCESO')", [user_id])
    conn.commit()

    follow_up_id = cursor.lastrowid

    # Insertar en la tabla detail_follow_up
    for celda_ruc in columna_ruc[1:]:
        valor_ruc = celda_ruc.value
        cursor.execute(
            "INSERT INTO detail_follow_up (follow_up_id, ruc_follow_up, final_estate) VALUES (%s, %s,'INACTIVO')", (follow_up_id, valor_ruc))
        conn.commit()

    conn.close()

    return redirect(url_for('operaciones.inactive_tracking'))
