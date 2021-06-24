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
        print('entro funcion')
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'SELECT * FROM T_PACIENTE WHERE COD_PACIENTE = {dni}'
        cursor.execute(query)
        row = cursor.fetchall()
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
        print('entro funcion')
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'SELECT * FROM FN_VERHORARIO({idEspecialidad})'
        cursor.execute(query)
        row = cursor.fetchall()
        if row:
            for i in row:
                resultado = list(i)
            return resultado
        else:
            return 0
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 



