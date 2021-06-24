from fastapi import Request, FastAPI, requests
import pyodbc

server = 'usilserv.database.windows.net'
database = 'clinicDB'
username = 'inteligencia'
password = '@ia202106'   
driver= '{ODBC Driver 17 for SQL Server}'
app = FastAPI()

#Url consultar paciente
@app.post('/dniPaciente')
async def consultaPaciente(request: Request):   
    try: 
        print('Entro al post')
        body = await request.json()
        nombre = consultarPaciente(body['dni'])
        print(f'Salio de la funcion {nombre}')
        return nombre
    except Exception as e :
        print(f'Error: {e}')   
        
@app.post('/postPrueba')
async def postPrueba(request:Request):
    body = await request.json()
    return body['dni']
    
@app.get('/pruebita')
async def pregunta():
    return 'Se colgo la api con exito, manco mamon'

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
            return resultado
        else:
            return 0
    except (Exception, pyodbc.Error) as e :
        print(f'Error: {e}') 


