from fastapi import Request, FastAPI
from BD import *

app = FastAPI()

#Url consultar paciente
@app.post('/dniPaciente')
async def consultaPaciente(request: Request):   
    try: 
        body = await request.json()
        dni = body['dni']
        nombre = consultarPaciente(dni)
        return nombre
    except Exception as e :
        return f'Error: {e}'   


#Obtener horarios disponibles
@app.post('/obtenerHorario')
async def obtenerHorario(request: Request):
    try:
        body = await request.json()
        idEspecialidad = body['idEspecialidad']
        horario = consultarHorario(idEspecialidad)
        return horario, body['nombre']
    except Exception as e :
        return f'Error: {e}' 

#Crear cita
@app.post('/crearCita')
async def crearCita(request: Request):
    try:
        body = await request.json()
        idHorario, dni = body['idHorario'], body['dni']
        nuevaCita = crear_Cita(idHorario, dni)
        return nuevaCita
    except Exception as e :
        return f'Error: {e}' 









