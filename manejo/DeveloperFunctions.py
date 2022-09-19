from modelo import clases
from manejo import manejo
from datetime import date

def buscarIdentificadorEnBiblioteca(biblioteca,identificador):
  for material in biblioteca.getCatalogo():
    if material.getIdentificador()==identificador:
      return True
  return False

def buscarPersonaEnBiblioteca(biblioteca,cedula):
  for persona in biblioteca.getUsuarios():
    if persona.getCedula()==cedula:
      return True
  return False

def listarCatalogo(biblioteca):
  for material in biblioteca.getCatalogo():
      print("Identificador: " , material.getCantidadActual() , "Titulo: " , material.getTitulo() , "Fecha del registro: " , material.getFechaRegistro() , "Cantidad reistrada: " , material.getCantidadRegistrada() , "Cantidad actual: " , material.getCantidadActual())

def listarPersonas(biblioteca):
  for persona in biblioteca.getUsuarios():
      print("Nombre: " , persona.getNombre() , "Cedula: " , persona.getCedula() , "Rol: " , persona.getRol() , "Libros prestados: " , persona.getLibrosPrestados())

def listarRegistro(biblioteca):
  for registro in biblioteca.getHistorial():
      print("identificador del material: " , registro.getIdentificador() , "Nombre de la persona: " , registro.getNombre() , "Cedula de la persona: " , registro.getCedula() , "Estado: " , registro.getEstado() , "Fecha: " , registro.getFecha())