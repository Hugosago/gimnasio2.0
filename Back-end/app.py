from fastapi import FastAPI
from routes.user import user
from routes.personas import persona
from routes.roles import rol
from routes.usuarios_roles import usuario_rol
from routes.membresias import membresia
from routes.miembros import miembros
from routes.transacciones import  transacciones

app=FastAPI()
app.include_router(user)
app.include_router(persona)
app.include_router(rol)
app.include_router(usuario_rol)
app.include_router(membresia)
app.include_router(miembros)
app.include_router(transacciones)
print("Hola bienvenido a mi backend")