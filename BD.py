import pyodbc
import json


with open('appsetings.json', 'r') as jsonFile:
    body = json.load(jsonFile)
    server = body['server']
    database = body['database']
    username = body['username']
    password = body['password']   
    driver = body['driver']


def consultarPaciente(dni):
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'SELECT TOP 1 * FROM T_PACIENTE WHERE COD_PACIENTE = {dni}'
        cursor.execute(query)
        row = cursor.fetchall()
        print(row)
        if row:
            for i in row:
                resultado = list(i)
            return resultado[1]
        else:
            return 0
    except (Exception, pyodbc.Error) as e :
       return f'Error: {e}'

def consultarHorario(idEspecialidad):    
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'SELECT TOP 1 * FROM FN_VERHORARIO({idEspecialidad})'
        cursor.execute(query)
        row = cursor.fetchall()
        respuesta = {}
        if row:
            for i in row:
                respuesta['codHorario'] = i[0]
                respuesta['dia'] = i[1]
                respuesta['hora'] = i[2]
                respuesta['codDoctor'] = i[3]
            return respuesta
        else:
            return 0
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 

def crearCita(idHorario, dni):    
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'EXEC SP_CREAR_CITA {idHorario}, {dni}'
        cursor.execute(query)
        cursor.commit()
        cursor.close()
        conn.close()
        return 1
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 

def verCitas(dni):    
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'SELECT * FROM FN_VERCITA({dni})'
        cursor.execute(query)
        row = cursor.fetchall()
        respuesta = []
        if row:
            for i in row:
                dictTemp = {"codCita" : i[0], "fecha": i[1], "hora" : i[2], "nombreCita" : i[3]}
                respuesta.append(dictTemp)
            return respuesta
        else: 
            return 0
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 

def eliminarBDCita(idCita):    
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'EXEC CANCELARCITA {idCita}'
        cursor.execute(query)
        cursor.commit()
        cursor.close()
        conn.close()
        return 1
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 



