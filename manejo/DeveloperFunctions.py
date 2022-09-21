from manejo import manejo
from modelo import clases
from datetime import date

def CrearUsuario(biblioteca, cedula, nombre, rol):
  if(manejo.buscarPersonaEnBiblioteca(biblioteca,cedula)):
      print("La persona ya se encuentra registrada")
  else:
      persona = clases.Persona(nombre, cedula, rol, 0)
      biblioteca.getUsuarios().append(persona)


def CrearMaterial(biblioteca,identificador,titulo,cantidad):
    fecha = date.today()
    material=clases.Material(identificador,titulo,fecha,cantidad,cantidad)
    biblioteca.getCatalogo().append(material)