from flask import render_template, request, redirect, url_for, session
from functools import wraps
import mysql.connector
from cnx import DB_CONFIG

def list_users():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('list_users')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None



def obtener_info_clientes():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('obtener_info_clientes')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None


def obtener_new_clientes():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('obtener_new_clientes')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None


def obtener_new_clientes_filtrados(ruc):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('obtener_info_clientes_filtrados', [ruc])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def obtener_info_clientes_filtrados(ruc):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('obtener_info_clientes_filtrados', [ruc])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None

def clientes_imp():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('clientes_imp')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None


def clientes_imp_filtrados(ruc):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('clientes_imp_filtrados', [ruc])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def obtener_info_clientes_contrato(contrato):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('obtener_info_clientes_contrato', [contrato])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None


def list_follow_up():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('list_follow_up')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None
    
def list_collection_monthly():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('list_collection_monthly')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None

def list_monthly_support():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('list_monthly_support')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None

def detail_follow_up(id_follow):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_follow_up', [id_follow])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None

def detail_collection(id_collection):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_collection', [id_collection])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None

def detail_MonthlySupport(register_id):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_MonthlySupport', [register_id])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def detail_followU(id_details):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_follow', [id_details])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None

def details_collection(id_details):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('details_collection', [id_details])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def detail_contact(id_details):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_contact', [id_details])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def details_contact(id_details):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('details_contact', [id_details])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def detail_Support(id_details):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_Support', [id_details])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    
def detail_contactS(id_details):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_contactS', [id_details])

        # Retrieve the results
        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error connecting to the database: {e}')
        return None
    

def detail_follow_update(id_follow, ruc_E, state_follow_up, reason_follow_up,
                  detail_follow_up):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('detail_follow_update', [id_follow, ruc_E, state_follow_up, reason_follow_up,
                  detail_follow_up])

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_implementation: {str(e)}")


def create_newAtention(register_id,ruc_support,contract_number,user_id,problem,module):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('create_newAtention', [register_id,ruc_support,contract_number,user_id,problem,module])

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_implementation: {str(e)}")


def register_follow_contact(detail_id, type_contact, comment_contact):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('register_follow_contact', [detail_id, type_contact, comment_contact])

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_implementation: {str(e)}")

def register_collection_contact(detail_id, type_contact, comment_contact):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('register_collection_contact', [detail_id, type_contact, comment_contact])

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_implementation: {str(e)}")

def register_support_contact(detail_id, type_contact, comment_contact):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('register_support_contact', [detail_id, type_contact, comment_contact])

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_implementation: {str(e)}")


def create_new_implementation(ruc, user_id,contract_number, pass_sun_boolean, pass_sun, pass_pass_sun, comercial_name, comercial_address, comercial_phone, comercial_email, taxes, secundary_user, pass_secundary_user, url_cd, pass_cd, expiration_cd, gr_pass, gr_id):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('create_new_implementation', [ruc, user_id, contract_number, pass_sun_boolean, pass_sun, pass_pass_sun, comercial_name, comercial_address,
                        comercial_phone, comercial_email, taxes, secundary_user, pass_secundary_user, url_cd, pass_cd, expiration_cd, gr_pass, gr_id])

        cursor.callproc('change_state_imp',[ruc,'EN PROCESO'])
        # Retrieve the results
        # Commit the changes to the database
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_implementation: {str(e)}")


def create_new_client(user_id, closure_type, ruc, social_name, legal_representative, doc_number, department, tax_address,
                      business_line, client_name, client_email, client_phone, implementor_name, implementor_email,
                      implementor_phone, plan, contract_type, stores_number, stores_conf, users_number, users_conf, link_contract,
                      fe, buy_cd, guides, initial_amount_plan, pending_amount, invoice_number, renew_amount, payment_date, start_date, end_date,
                      comment_i, comment_c, sale_type, p_estado_imp):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('create_new_client', [user_id, closure_type, ruc, social_name, legal_representative, doc_number, department, tax_address,
                                              business_line, client_name, client_email, client_phone, implementor_name, implementor_email,
                                              implementor_phone, plan, contract_type, stores_number, stores_conf, users_number, users_conf, link_contract,
                                              fe, buy_cd, guides, initial_amount_plan, pending_amount, invoice_number, renew_amount, payment_date, start_date, end_date,
                                              comment_i, comment_c, sale_type, p_estado_imp])

        # Retrieve the results
        # Commit the changes to the database
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in create_new_client: {str(e)}")

def new_company(user_id,ruc,contract_number,support_email,support_pas):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Call a stored procedure to retrieve filtered client data
        cursor.callproc('new_company', [user_id,ruc,contract_number,support_email,support_pas])

        cursor.callproc('change_state_imp',[ruc,'FINALIZADO'])
        # Retrieve the results
        # Commit the changes to the database
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in new_company: {str(e)}")

def new_train(user_id,user_id_resp,ruc,contract_number,url_train,date_train,hour_train):
    try:
        # Establish the database connection using DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llamas al procedimiento almacenado y obtienes los resultados
        cursor.callproc('list_train_ruc', [ruc])

        for result in cursor.stored_results():
            rows = result.fetchall()
            number_of_capacitaciones = len(rows)

        if number_of_capacitaciones == 0:
            cursor.execute("UPDATE company SET status_train = 'AGENDADA' WHERE ruc = %s", [ruc])
            cursor.callproc('new_train', [user_id,user_id_resp,ruc,contract_number,url_train,date_train,hour_train])

        else:
            cursor.callproc('new_train', [user_id,user_id_resp,ruc,contract_number,url_train,date_train,hour_train])


        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        # Handle any exceptions that might occur during the database operation
        print(f"Error in new_company: {str(e)}")



def list_trains():
    try:
        # Establece la conexión a tu base de datos utilizando la configuración de DB_CONFIG
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Llama al procedimiento almacenado
        cursor.callproc('list_train')

        # Recupera los resultados
        for result in cursor.stored_results():
            data = result.fetchall()

        # Cierra el cursor y la conexión solo si se crearon con éxito
        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None