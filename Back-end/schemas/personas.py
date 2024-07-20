from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
import enum

class PersonaBase(BaseModel):
    Titulo_Cortesia: str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Fecha_Nacimiento: date
    Fotografia: str
    Genero: enum
    Tipo_Sangre: enum
    Estatus: bool
    Fecha_Registro : datetime
    Fecha_Actualizacion: datetime


class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(PersonaBase):
    pass

class Persona(PersonaBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True


