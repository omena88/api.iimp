from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class UserData(BaseModel):
    whatsapp_phone: str = Field(..., alias="whatsapp phone")
    source: str
    nombre_completo: str = Field(..., alias="nombre completo")
    dni: str

app = FastAPI(
    title="API de Recepción de Datos",
    description="Una API simple para recibir datos de usuario y confirmar su recepción.",
    version="1.0.0",
)

@app.post("/datos/")
async def recibir_datos(data: UserData):
    """
    Recibe los datos del usuario, los valida y devuelve un mensaje de confirmación.
    """
    return {
        "status": "success",
        "message": f"Datos recibidos de {data.nombre_completo} con DNI: {data.dni}"
    }

@app.get("/")
def health_check():
    """
    Endpoint de health check para verificar que la API está funcionando.
    """
    return {"status": "ok", "message": "API funcionando correctamente."} 