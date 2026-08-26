from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from fastapi import FastAPI

# Tipo genérico para la propiedad 'data'
T = TypeVar('T')

# 1. Definición del Estándar de Respuesta (ApiResponse)
class ApiResponse(BaseModel, Generic[T]):
    success: bool
    statusCode: int
    message: str
    data: Optional[T] = None

# 2. Inicialización de FastAPI
app = FastAPI()

# Ejemplo de Endpoint usando el estándar
@app.get("/", response_model=ApiResponse[dict])
def read_root():
    return ApiResponse(
        success=True,
        statusCode=200,
        message="Operación exitosa",
        data={"mensaje": "Hola Mundo"}
    )
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)