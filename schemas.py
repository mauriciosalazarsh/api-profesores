from pydantic import BaseModel
class Professor(BaseModel):
    nombre: str
    apellido: str
    título: str
    especialidad: str
