from fastapi import Request, FastAPI, Response
from BD import *

app = FastAPI()

#Url consultar paciente
@app.post('/dniPaciente')
async def consultaPaciente(request: Request):    
    body = await request.json()
    nombre = consultarPaciente(body['dni'])
    return nombre

@app.get('/pruebita')
async def pregunta():
    return 'Se colgo la api con exito'
    
#Url crear cita

#Url eliminar cita

#Url consulta horarios

