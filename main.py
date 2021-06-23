from fastapi import Request, FastAPI
from BD import *

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

@app.get('/pruebita')
async def pregunta():
    return 'Se colgo la api con exito, manco mamon'

#Url crear cita

#Url eliminar cita

#Url consulta horarios

