from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"set_attributes": {"responseApi": False}},
    )

@app.post("/datos/")
async def recibir_datos(data: UserData):
    """
    Recibe los datos del usuario y devuelve la respuesta en el formato especificado.
    """
    return {"set_attributes": {"responseApi": True}}

@app.get("/")
def health_check():
    """
    Endpoint de health check para verificar que la API está funcionando.
    """
    return {"status": "ok", "message": "API funcionando correctamente."} 