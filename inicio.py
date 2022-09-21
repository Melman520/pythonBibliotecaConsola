from manejo import manejo
from manejo import DeveloperFunctions as df
from modelo import clases

biblioteca = clases.Biblioteca()


while True:
    opcion = input("\n 1.Registrar material \n 2.Registrar una persona \n 3.Eliminar persona \n 4.Registrar un prestamo \n 5.Registrar una devolucion \n 6.Incrementar cantidad registrada de un material \n 7. Consultar el historial de la biblioteca \n 8.Salir \n")
    if opcion == "1":
        manejo.registrarMaterialEnBiblioteca(biblioteca)
    elif opcion == "2":
        manejo.registrarPersonaEnBiblioteca(biblioteca)
        manejo.listarPersonas(biblioteca)
    elif opcion == "3":
        manejo.eliminarPersona(biblioteca)
        manejo.listarPersonas(biblioteca)
    elif opcion == "4":
        manejo.listarCatalogo(biblioteca)
        manejo.validarUsuario(biblioteca, "prestamo")
    elif opcion == "5":
        manejo.listarCatalogo(biblioteca)
        manejo.validarUsuario(biblioteca,"devolucion")
    elif opcion == "6":
        manejo.aumentarunidades(biblioteca)
    elif opcion == "7":
        manejo.listarRegistro(biblioteca)
    elif opcion == "8":
        print("Gracias por usar el programa")
        quit()
    elif opcion == "9": #Crear usuarios de ejemplo
        df.CrearUsuario(biblioteca, 1 , "Nelson", "estudiante")
        df.CrearUsuario(biblioteca, 2 , "Davinson", "profesor")
        df.CrearUsuario(biblioteca, 3 , "Jimmy", "administrativo")
        manejo.listarPersonas(biblioteca)
    elif opcion == "10":    #Crear materiales de ejemplo
        df.CrearMaterial(biblioteca, 111, "Cien años de soledad", 10)
        df.CrearMaterial(biblioteca, 222, "El señor de los anillos", 15)
        df.CrearMaterial(biblioteca, 333, "El Quijote de La Mancha", 20)
    elif opcion == "11":
        manejo.listarCatalogo(biblioteca)
        manejo.listarPersonas(biblioteca)
    else:
        print("Ingrese una opción valida")