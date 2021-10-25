def listarCursos(cursos):
    contador=1
    print("\nMostrando cursos\n")
    for cursoActual in cursos:
        dato=("{0}. |Codigo---->{1}|\n |Nombre---->{2}|\n |Duracion--->{3} hs|\n")
        #                            codigo         nombre        duracion
        print(dato.format(contador,cursoActual[0],cursoActual[1],cursoActual[2]))
        contador=contador+1
    print("\n")


def crearCurso():
    codigoCorrecto=False
    while(not codigoCorrecto):

        codigo=input("Ingrese el codigo del curso->")
        if(len(codigo)==6):
            codigoCorrecto=True

        else:
            codigoCorrecto=False
            print("el codigo debe tener 6 digitos")

    nombre=input("Ingrese el nombre del curso->")
    
    
    duracionCorrecta=False
    while(not duracionCorrecta):
        duracion=input("Ingrese la duracion del curso->")
        
        try:
            float(duracion)
            duracionCorrecta=True
        except ValueError:
            print ("Not a float")

       
     
    nuevoCurso=(codigo,nombre,duracion)
    return nuevoCurso
def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo=False
    codigoAmodificar=isNumber("Ingrese el codigo del curso a modificar->")
    for cur in cursos:
       

        if(cur[0]==codigoAmodificar):
            
            existeCodigo=True
            break
    
    if(existeCodigo):

        print("modificando curso---")

        nombre=input("Ingrese el nuevo nombre del curso->")

        duracionCorrecta=False
        while(not duracionCorrecta):
            duracion=input("Ingrese la nueva duracion del curso->")

            try:
                float(duracion)
                duracionCorrecta=True
            except ValueError:
                print ("Not a float")

        curso=(codigoAmodificar,nombre,duracion)
    else:
        curso=None

    return curso

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    codigoEliminar=None
    existeCodigo=False
    codigoEliminar=isNumber("Ingrese el codigo del curso a eliminar->")
    for cur in cursos:
        

        if(cur[0]==codigoEliminar):
            
            existeCodigo=True
            break
    
    if not existeCodigo:
        codigoEliminar= ""

    return codigoEliminar

def isNumber(inputText):
    valorCorrecto=False
    while(not valorCorrecto):
       
        x=input(inputText)
  
        if(x.isnumeric()):
            valorCorrecto=True
            x=int(x)
        else:
            print("porfavor ingrese un valor numerico")
    return x