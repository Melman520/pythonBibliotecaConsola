from pickle import TRUE
from modelo import clases
from manejo import DeveloperFunctions
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
      print("Identificador:" , material.getIdentificador() , "Titulo:" , material.getTitulo() , "Fecha del registro:" , material.getFechaRegistro() , "Cantidad reistrada:" , material.getCantidadRegistrada() , "Cantidad actual:" , material.getCantidadActual())

def listarPersonas(biblioteca):
  for persona in biblioteca.getUsuarios():
      print("Nombre:" , persona.getNombre() , "Cedula:" , persona.getCedula() , "Rol:" , persona.getRol() , "materiales prestados:" , persona.getLibrosPrestados())

def listarRegistro(biblioteca):
  for registro in biblioteca.getHistorial():
      print("identificador del material:" , registro.getIdentificador() , "Nombre de la persona:" , registro.getNombre() , "Cedula de la persona:" , registro.getCedula() , "Estado:" , registro.getEstado() , "Fecha:" , registro.getFecha())


def aumentarunidades(biblioteca):
  try:
    identificador=input("ingrese el identificador del material: ")
    cantidad = int(input("Ingrese la cantidad de unidades que desea agregar: "))
    for material in biblioteca.getCatalogo():
      encontrado = True
      if material.getIdentificador()==identificador:
        material.setCantidadActual(material.getCantidadActual()+cantidad)
        print("Unidades agregadas con exito")
    
    if encontrado == False:
      print("No se encontro material con ese identificador")
  except:
    print("valor invalido")

def registrarMaterialEnBiblioteca(biblioteca):
  identificador=input("ingrese el identificador del material: ")
  if(buscarIdentificadorEnBiblioteca(biblioteca,identificador)):
    print("ese material ya se encuentra registrado")
  else:
    titulo = input("ingrese el titulo del material: ")
    fecha = date.today()
    validarNumero=True
    while(validarNumero):
      try:
        cantidad = int(input("ingrese la cantidad inicial a registrar: "))
        validarNumero=False
        if cantidad <= 0:
          print("La cantidad debe ser mayor a cero")
          validarNumero=True
      except:
        print("no ingreso un numero valido")
    material=clases.Material(identificador,titulo,fecha,cantidad,cantidad)
    biblioteca.getCatalogo().append(material)

def registrarPersonaEnBiblioteca(biblioteca):
  try:
    cedula = int(input("ingrese la cedula: "))
    if(buscarPersonaEnBiblioteca(biblioteca,cedula)):
      print("La persona ya se encuentra registrada")
    else:
      nombre = input("Ingrese el nombre: ")
      while True:
        rol = input("Ingrese el rol Estudiante, Profesor o Administrativo: ")
        if rol.lower() != "estudiante" and rol.lower() != "profesor" and rol.lower() != "administrativo":
          print("ingrese un rol valido")
        else:
          break
      persona = clases.Persona(nombre, cedula, rol, 0)
      biblioteca.getUsuarios().append(persona)
  except:
    print("Cedula invalida, volviendo al menu inicial...")

def eliminarPersona(biblioteca):
  try:
    cedula = int(input("Ingrese la cedula de la persona a borrar \n"))
    for persona in biblioteca.getUsuarios():
      if persona.getCedula()==cedula:
        pencontrado = True
        if persona.getLibrosPrestados == 0:
          biblioteca.getUsuarios().remove(persona)
          print("Persona borrada exitosamente")
        else:
          print("No se puede eliminar a la persona si tiene material prestado")

    if pencontrado == False:
      print("No se encontró ninguna persona con esa cedula")
  except:
    print("Cedula invalida, volviendo al menu inicial...")

def validarRol(biblioteca,persona, df):
  if persona.getRol() == "profesor" and df == "prestamo":
    if persona.getLibrosPrestados() <3:
      prestamo(biblioteca,persona)
    else:
      print("Denegado: Los profesores solo pueden prestar 3 materiales")
  
  if persona.getRol() == "estudiante" and df == "prestamo":
    if persona.getLibrosPrestados() <5:
      prestamo(biblioteca,persona)
    else:
      print("Denegado: Los estudiantes solo pueden prestar 5 materiales")

  if persona.getRol() == "administrativo" and df == "prestamo":
    if persona.getLibrosPrestados() <1:
      prestamo(biblioteca,persona)
    else:
      print("Denegado: Los administrativos solo pueden prestar 1 material")
  
  if df == "devolucion":
    devolucion(biblioteca, persona)


def validarUsuario(biblioteca,df):
  try:
    cedula = int(input("Ingrese su cedula de usuario registrado: "))
    for persona in biblioteca.getUsuarios():
      if persona.getCedula()== cedula:
        validarRol(biblioteca, persona, df)
        encontrado = True
    if encontrado == False:
        print("usuario no registrado")
  except:
    print("numero invalido")



def devolucion(biblioteca, persona):
  cedula = persona.getCedula()
  nombre = persona.getNombre()
  identificador = input("Ingrese el identificador del material que desea devolver: \n")
  for material in biblioteca.getCatalogo():
    if (material.getIdentificador()==identificador):
      if persona.getLibrosPrestados()>0:
        persona.setLibrosPrestados(persona.getLibrosPrestados()-1)
        material.setCantidadActual(material.getCantidadActual()+1)
        print("Material devuelto exitosamente")
        guardarRegistro(biblioteca, identificador, "Devuleto",nombre, cedula)
      else:
        print("No tienes ese libro")


def prestamo(biblioteca, persona):
  cedula = persona.getCedula()
  nombre = persona.getNombre()
  identificador = input("Ingrese el identificador del material que desea prestar: \n")
  for material in biblioteca.getCatalogo():
    if (material.getIdentificador()==identificador):
      if material.getCantidadActual() > 0:
        material.setCantidadActual(material.getCantidadActual()-1)
        persona.setLibrosPrestados(persona.getLibrosPrestados()+1)
        print("Material prestado exitosamente")
        guardarRegistro(biblioteca, identificador, "Prestado", nombre, cedula)
      else:
        print("Lo sentimos, ya no queda de ese material")
    else:
      print("No se encontró ningun material con ese identificador")


def guardarRegistro(biblioteca, identificador, estado, nombre, cedula):
  fecha = date.today()
  registro = clases.Registro(identificador, estado, nombre, cedula, fecha)
  biblioteca.getHistorial().append(registro)