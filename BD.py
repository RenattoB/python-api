import psycopg2

def consultarPaciente(dni):
    try:
        conn = psycopg2.connect(host = '127.0.0.1', port = '5432', database = 'ClinicDB', user = 'postgres', password = 'Morshi1801')
        cursor = conn.cursor()
        query = f'SELECT * FROM T_PACIENTE WHERE COD_PACIENTE = (%s) LIMIT 1'
        cursor.execute(query, (dni,))
        row = cursor.fetchall()
        print(row)
        if row:
            for i in row:
                resultado = list(i)
            return resultado[1]
        else:
            return 0
    except (Exception, psycopg2.Error) as e :
        print('Hubo un error durante la conexión de la BD: '+ str(e) + '\n')
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print('Se cerro la conexion con la BD\n')



#Ejemplos stores
def insertarTramite(codAlumno):
    error = 0
    try:
        conn = psycopg2.connect(host = '127.0.0.1', port = '5432', database = 'usilBot', user = 'postgres', password = 'Morshi1801')
        cursor = conn.cursor()
        cursor.execute('CALL SP_CREAR_TRAMITE(%s);', (codAlumno,))
        conn.commit()    
    except (Exception, psycopg2.Error) as e :
        print('Hubo un error durante la conexión de la BD: '+ str(e) + '\n')
        error = 1        
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print('Se cerro la conexion con la BD\n')
            if error:
                return 'Ya existe ese tramite con este codigo de alumno'
            else:
                return 'Se registro su trámite con exito'
                

def consultarEstadoTramite(codAlumno):
    try:
        conn = psycopg2.connect(host = '127.0.0.1', port = '5432', database = 'usilBot', user = 'postgres', password = 'Morshi1801')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FN_ESTADO_TRAMITES(%s)', (codAlumno,))
        row = cursor.fetchall()
        print(row)
        if row:
            return row            
        else:
            return 'No tiene ningún trámite activo por el momento'
    
    except (Exception, psycopg2.Error) as e :
        print('Hubo un error durante la conexión de la BD: '+ str(e) + '\n')
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print('Se cerro la conexion con la BD\n')
            
