from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session
from functools import wraps
import mysql.connector
import mysqlx
from app.models import obtener_info_clientes, obtener_info_clientes_contrato, obtener_info_clientes_filtrados, create_new_client
from cnx import DB_CONFIG

ventas_bp = Blueprint('ventas', __name__)


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'user_name' in session and 'user_password' in session:
            return route_function(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper


@ventas_bp.route('/sale', methods=['GET', 'POST'])
@login_required
def sale():
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

    return render_template('ventas/sale.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, lista_clientes=lista_clientes)


@ventas_bp.route('/searchSale', methods=['GET', 'POST'])
@login_required
def searchSale():
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

    return render_template('ventas/searchSale.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area, cliente=cliente)


@ventas_bp.route('/newSale')
@login_required
def newSale():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    return render_template('ventas/newSale.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area,)


@ventas_bp.route('/newSaleE', methods=['GET', 'POST'])
@login_required
def newSaleE():
    user_id = session.get('user_id')

    if request.method == 'POST':

        ruc = request.form.get('ruc')
        motivoE = request.form.get('motivoE')
        datePagoE = request.form.get('datePagoE')
        initialE = request.form.get('initialE')
        totalE = request.form.get('totalE')
        nroFacE = request.form.get('nroFacE')
        departamentoE = request.form.get('departamentoE')
        provinciaE = request.form.get('provinciaE')
        distritoE = request.form.get('distritoE')
        dirE = request.form.get('dirE')
        reference = request.form.get('reference')
        linkUbication = request.form.get('linkUbication')
        nroDocE = request.form.get('nroDocE')
        namesE = request.form.get('namesE')
        nroCelE = request.form.get('nroCelE')
        typeE = request.form.get('typeE')
        delivery = request.form.get('delivery')
        if 'delivery' in request.form:
            amountE = request.form.get('amountE')
        else:
            amountE = 0

        nroFacD = request.form.get('nroFacD')
        dateE = request.form.get('dateE')
        responsableE = request.form.get('responsableE')
        comentaryE = request.form.get('comentaryE')
        TipoVenta = 'EQUIPO'
        Estado = 'PENDIENTE'

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ventaequipo (user_id, ruc, motivoE, datePagoE, initialE, totalE, nroFacE, departamentoE, provinciaE, distritoE, dirE, reference, linkUbication, nroDocE, namesE, nroCelE, typeE, delivery, amountE, nroFacD, dateE, responsableE, comentaryE, TipoVenta, Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [user_id, ruc, motivoE, datePagoE, initialE, totalE, nroFacE, departamentoE, provinciaE, distritoE, dirE, reference, linkUbication, nroDocE, namesE, nroCelE, typeE, delivery, amountE, nroFacD, dateE, responsableE, comentaryE, TipoVenta, Estado])
        conn.commit()

        idVentaE = cursor.lastrowid

        productoCounter = request.form.get('productoCounter')

        # Datos de los productos
        productos = []
        for i in range(1, int(request.form.get('productoCounter', 0)) + 1):
            nombre = request.form.get(f'nameE{i}')
            cantidad = request.form.get(f'quantityE{i}')

            if nombre and cantidad:
                producto = {
                    'nombre': nombre,
                    'cantidad': cantidad
                    
                }
                productos.append(producto)

        for producto in productos:
            nombre = producto['nombre']
            cantidad = producto['cantidad']
            
            cursor.execute("INSERT INTO EquipoVendido (nameE, quantityE, idVentaE) VALUES (%s, %s, %s)",(nombre, cantidad, idVentaE)
    )
            conn.commit()
    
    return redirect(url_for('ventas.saleE'))

@ventas_bp.route('/extra_sale', methods=['GET', 'POST'])
@login_required
def extra_sale():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    if request.method == 'POST':

        ruc_extra = request.form.get('ruc_extra')
        contract_extra = request.form.get('contract_extra')
        reason_extra = request.form.get('reason_extra')
        amount_extra = request.form.get('amount_extra')
        nro_fac_extra = request.form.get('nro_fac_extra')
        pay_day_extra = request.form.get('pay_day_extra')
        nro_doc_extra = request.form.get('nro_doc_extra')
        name_extra = request.form.get('name_extra')
        num_client_extra = request.form.get('num_client_extra')
        commentry_extra = request.form.get('commentry_extra')
        type_extra = request.form.get('type_extra')

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO extra (user_id, ruc_extra, contract_extra, reason_extra, amount_extra, nro_fac_extra, pay_day_extra, nro_doc_extra, name_extra, num_client_extra, commentry_extra, type_extra) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)", [user_id, ruc_extra, contract_extra, reason_extra, amount_extra, nro_fac_extra, pay_day_extra, nro_doc_extra, name_extra, num_client_extra, commentry_extra, type_extra])
        conn.commit()

        return redirect(url_for('ventas.extraSale'))


@ventas_bp.route('/validar_client', methods=['GET'])
def validar_client():
    ruc = request.args.get('ruc')

    try:
        conn = mysqlx.connector.connect(**DB_CONFIG)
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


@ventas_bp.route('/newClient', methods=['GET', 'POST'])
@login_required
def newClient():
    user_id = session.get('user_id')

    if request.method == 'POST':
        closure_type = request.form.get('closure_type')
        ruc = request.form.get('ruc')
        social_name = request.form.get('social_name')
        legal_representative = request.form.get('legal_representative')
        business_line = request.form.get('business_line')
        doc_number = request.form.get('doc_number')
        department = request.form.get('department')
        tax_address = request.form.get('tax_address')
        client_name = request.form.get('client_name')
        client_email = request.form.get('client_email')
        client_phone = request.form.get('client_phone')

        if 'implementadorCheckbox' in request.form:
            implementor_name = request.form.get('implementor_name')
            implementor_email = request.form.get('implementor_email')
            implementor_phone = request.form.get('implementor_phone')
        else:
            implementor_name = ""
            implementor_email = ""
            implementor_phone = ""

        plan = request.form.get('plan')
        contract_type = request.form.get('contract_type')
        stores_number = request.form.get('stores_number')
        users_number = request.form.get('users_number')
        link_contract = request.form.get('link_contract')
        initial_amount_plan = request.form.get('initial_amount_plan')
        pending_amount = request.form.get('pending_amount')
        renew_amount = request.form.get('renew_amount')
        invoice_number = request.form.get('invoice_number')
        payment_date = request.form.get('payment_date')
        stores_conf = request.form.get('stores_conf')
        users_conf = request.form.get('users_conf')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        if 'fe' in request.form:
            fe = True
        else:
            fe = False

        if 'buy_cd' in request.form:
            buy_cd = True
        else:
            buy_cd = False

        if 'guides' in request.form:
            guides = True
        else:
            guides = False

        comment_i = request.form.get('comment_i')
        comment_c = request.form.get('comment_c')
        sale_type = "SISTEMA"
        p_estado_imp = 'PENDIENTE'

        create_new_client(user_id, closure_type, ruc, social_name, legal_representative, doc_number, department, tax_address,
                          business_line, client_name, client_email, client_phone, implementor_name, implementor_email,
                          implementor_phone, plan, contract_type, stores_number, stores_conf, users_number, users_conf, link_contract,
                          fe, buy_cd, guides, initial_amount_plan, pending_amount, invoice_number, renew_amount, payment_date, start_date, end_date,
                          comment_i, comment_c, sale_type, p_estado_imp)

        return redirect(url_for('ventas.sale'))


@ventas_bp.route('/saleE')
@login_required
def saleE():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    return render_template('ventas/saleE.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area,)


@ventas_bp.route('/extraSale')
@login_required
def extraSale():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    user_password = session.get('user_password')
    user_full_name = session.get('user_full_name')
    user_area = session.get('user_area')

    return render_template('ventas/extraSale.html', user_id=user_id, user_name=user_name, user_password=user_password, user_full_name=user_full_name, user_area=user_area,)
