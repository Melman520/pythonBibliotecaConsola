class Biblioteca:
  def __init__(self):
    self._catalogo=[]
    self._usuarios=[]
    self._historial=[]
  def getCatalogo(self):
    return self._catalogo
  def setCatalogo(self, catalogo):
    self._catalogo=catalogo
  def getUsuarios(self):
    return self._usuarios
  def setUsuarios(self, usuarios):
    self._usuarios= usuarios
  def getHistorial(self):
    return self._historial
  def setHistorial(self, historial):
    self._historial= historial
  
class Material:
  def __init__(self,identificador,titulo,fechaRegistro,cantidadRegistrada,cantidadActual):
    self._identificador=identificador
    self._titulo=titulo
    self._fechaRegistro=fechaRegistro
    self._cantidadRegistrada=cantidadRegistrada
    self._cantidadActual=cantidadActual
  def getIdentificador(self):
    return self._identificador
  def setIdentificador(self, identificador):
    self._identificador = identificador
  def getTitulo(self):
    return self._titulo
  def setTitulo(self, titulo):
    self._titulo = titulo
  def getFechaRegistro(self):
    return self._fechaRegistro
  def setFechaRegistro(self, fechaRegistro):
    self._fechaRegistro = fechaRegistro
  def getCantidadRegistrada(self):
    return self._cantidadRegistrada
  def setCantidadRegistrada(self, cantidadRegistrada):
    self._cantidadRegistrada = cantidadRegistrada
  def getCantidadActual(self):
    return self._cantidadActual
  def setCantidadActual(self, cantidadActual):
    self._cantidadActual = cantidadActual

class Persona:
  def __init__(self, nombre,cedula,rol,librosPrestados):
    self._nombre=nombre
    self._cedula=cedula
    self._rol=rol
    self._librosPrestados=librosPrestados
  def getNombre(self):
    return self._nombre
  def setNombre(self, nombre):
    self._nombre = nombre
  def getCedula(self):
    return self._cedula
  def setCedula(self, cedula):
    self._cedula = cedula
  def getRol(self):
    return self._rol
  def setRol(self, rol):
    self._rol = rol
  def getLibrosPrestados(self):
    return self._librosPrestados
  def setLibrosPrestados(self, librosPrestados):
    self._librosPrestados	 = librosPrestados

class Registro:
  def __init__(self, identificador, estado, nombre, cedula, fecha):
    self._identificador=identificador
    self._estado=estado
    self._nombre=nombre
    self._cedula=cedula
    self._fecha=fecha
  def getIdentificador(self):
    return self._identificador
  def setIdentificador(self, identificador):
    self._identificador = identificador
  def getEstado(self):
    return self._estado
  def setEstado(self, estado):
    self._estado = estado
  def getNombre(self):
    return self._nombre
  def setNombre(self, nombre):
    self._nombre = nombre
  def getCedula(self):
    return self._cedula
  def setCedula(self, cedula):
    self._cedula = cedula
  def getFecha(self):
    return self._fecha
  def setFecha(self, fecha):
    self._fecha = fecha