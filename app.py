from BD.conexion import DAO
import funciones
import os
from mysql.connector import Error
def menuPrincipal():
    continuar=True
   
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            os.system("pause")
            os.system("cls")
            print("<========-MENU PRINCIPAL-=========>")
            print("1-listar cursos--")
            print("2-registrar curso--")
            print("3-modificar curso--")
            print("4-eliminar curso--")
            print("5-salir--")
            print("-----------------------------------")
            opcion=input("Seleccione una opcion: ")
         
            if(not checkInput(opcion)): 
                opcionCorrecta=False
                print("El valor ingresado no es un entero")
            else:
                opcion=int(opcion)
            
            if(checkInput(opcion)):
                
                if(opcion<1 or opcion>5):
                    opcionCorrecta=False
                    print("opcion incorrecta ingrese nuevamente....")
                elif(opcion==5):
                    print("saliendo del sistema hasta luego...")
                    os.system("pause")
                    os.system("cls")
                    continuar=False
                    
                    break
                else:
                    opcionCorrecta=True
                    ejecutarOpcion(opcion)


def menu(dao,opcion):
    if opcion==1:
        print("Listar cursos")
        try:
            cursos=dao.listarCursos()
            if len(cursos)>0:
                funciones.listarCursos(cursos)
               
            else:
                print("no se encontraron cursos")
        except:
                print("error")
        
    elif opcion==2:
        print("Registro")
        curso=funciones.crearCurso()
        print(curso[0])
        print(curso[1])
        print(curso[2])
        try:
            dao.registrarCurso(curso)
        except Error as ex:
                print("error al intentar registrar el curso: {0}".format(ex))
    elif opcion==3:
        print("Modificar")
        try:
            cursos=dao.listarCursos()
            if len(cursos)>0:
                cursoModificado=funciones.pedirDatosActualizacion(cursos)
                if(cursoModificado):
                    dao.actualizarCurso(cursoModificado)
                else:
                    print("codigo del curso a actualizar no encontrado")
               
            else:
                print("no se encontraron cursos")
        
        except:
                print("error")
    elif opcion==4:
        
        try:
            print("Eliminar")
            cursos=dao.listarCursos()
            if len(cursos)>0:
              
                codigoAeliminar=funciones.pedirDatosEliminacion(cursos)

                if(not(codigoAeliminar=="")):
                    dao.eliminarCurso(codigoAeliminar)
                else:
                    print("curso no encontrado")
               
            else:
                print("no se encontraron cursos")

        except:
                print("error")
    else:
        print("opcion no valida")

def ejecutarOpcion(opcion):
    dao=DAO()
    menu(dao,opcion)


def checkInput(string):
    try:
        val = int(string)
        return True
    except ValueError:
       
        return False


menuPrincipal()