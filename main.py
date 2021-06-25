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
        return horario
    except Exception as e :
        return f'Error: {e}' 

#Crear cita
@app.post('/crearCita')
async def reservarCita(request: Request):
    try:
        body = await request.json()
        idHorario, dni = body['idHorario'], body['dni']
        nuevaCita = crearCita(idHorario, dni)
        return nuevaCita
    except Exception as e :
        return f'Error: {e}' 

#Ver Citas
@app.post('/verCitasPaciente')
async def reservarCita(request: Request):
    try:
        body = await request.json()
        dni = body['dni']
        citas = verCitas(dni)
        return {"citas" : citas}
    except Exception as e :
        return f'Error: {e}' 

#Eliminar cita         

@app.post('/eliminarCita')
async def eliminarCita(request: Request):
    try:
        body = await request.json()
        idCita = body['idCita']
        citaEliminada = eliminarBDCita(idCita)
        return citaEliminada
    except Exception as e :
        return f'Error: {e}'

@app.get('/arrayPrueba')
def arregloPrueba():
    dict = {
        "nombres": [{"id": "12", "nombre": "Renatto", "apellido":"Baca"} , {"id": "15","nombre" : "Dariel", "apellido": "Solorzano"}, {"id": "20","nombre" : "Julio", "apellido": "Ponce"}] 
    }
    return dict







