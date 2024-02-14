#samplepythonapi
from fastapi import FastAPI

app: FastAPI = FastAPI(
    tittle = "SamplePythonApi",
    description = "USBCS202401"
)



@app.get(
    "/operacionGet",
    summary = "Operacion Get",
    tags = ["Get"])
async def operacion_get(dato_entrada: str):
    return dato_entrada