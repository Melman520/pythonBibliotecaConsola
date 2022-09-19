from manejo import manejo
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
    else:
        print("Ingrese una opción valida")