import pyodbc

server = 'usilserv.database.windows.net'
database = 'clinicDB'
username = 'inteligencia'
password = '@ia202106'   
driver= '{ODBC Driver 17 for SQL Server}'

def consultarPaciente(dni):
    try:
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
        print(f'Error: {e}') 




