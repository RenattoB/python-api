import pyodbc
import json
from datetime import datetime, timedelta


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
        query = f'SELECT TOP 1 * FROM T_PACIENTE WHERE ID_PACIENTE = {dni}'
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

def consultarHorario(idEspecialidad, dia):    
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'SELECT * FROM FN_VERHORARIOS ((?) ,(?))'
        cursor.execute(query, (idEspecialidad, dia, ))
        row = cursor.fetchall()
        respuesta = []
        recibioHorarios = False
        recibioRecomendacion = False
        if len(row) == 1:
            if row[0][0] == None:
                fechaRecomendada = None
                while recibioHorarios == False:
                    dia = datetime.strptime(dia, "%Y-%m-%d")
                    dia = dia + timedelta(days=1)
                    dia = datetime.strftime(dia, "%Y-%m-%d")
                    query2 = f'SELECT TOP 1 * FROM FN_VERHORARIOS ((?) ,(?))'
                    cursor.execute(query2, (idEspecialidad, dia, ))
                    row = cursor.fetchall()
                    if len(row) != 0:
                        if row[0][0] != None:
                            recibioHorarios = True
                            recibioRecomendacion = True
                            fechaRecomendada = dia
                            print(f'fecha recomendada: {fechaRecomendada}')
                            break
                return {"horarios": 0, "recibioRecomendacion": recibioRecomendacion, "fechaRecomendada": fechaRecomendada}
        else:
            recibioHorarios = True
        if row:
            for i in row:
                dictTemp = {'idDoctor': i[0], 'dia': i[1], 'horaInicio': i[2], 'horaFin': i[3]}
                respuesta.append(dictTemp)
            return {"horarios": respuesta, "recibioRecomendacion": recibioRecomendacion}
        else:
            return {"horarios" : 0, "recibioRecomendacion": recibioRecomendacion}
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 

#print(consultarHorario(10, '2021-06-28'))

def crearCita(idDoctor, idPaciente, fecha, horaInicio, horaSalida):    
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        query = f'EXEC SP_CREARCITA ?, ?, ?, ?, ?'
        cursor.execute(query, (idDoctor, idPaciente, fecha, horaInicio, horaSalida, ))
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
        query = f'SELECT * FROM FN_VERCITA ({dni}) ORDER BY FECHA, HORA_INICIO'
        cursor.execute(query)
        row = cursor.fetchall()
        respuesta = []
        if row:
            for i in row:
                dictTemp = {"codCita" : i[0], "fecha": i[1], "horaInicio" : i[2], "horaSalida" : i[3], "especialidad" : i[4]}
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
        query = f'EXEC SP_ELIMINARCITA {idCita}'
        cursor.execute(query)
        cursor.commit()
        cursor.close()
        conn.close()
        return 1
    except (Exception, pyodbc.Error) as e :
        return f'Error: {e}' 



