import mysql.connector
from mysql.connector import Error

class DAO():#DAO:Data Access Object
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123mielADOargentina',
                db='universidad'
            )
            
        except Error as ex:
            print("error al intentar la conexion: {0}".format(ex))

    def listarCursos(self):
        if(self.conexion.is_connected()):
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")#seleccionamos la informacion ordenandola de forma asc
                resultados=cursor.fetchall()#la traemos al programa y almacenamos la lista de tuplas en resultados
                return resultados
            except Error as ex:
                print("error al intentar la conexion: {0}".format(ex))


    def registrarCurso(self,curso):
        if(self.conexion.is_connected()):
            try:
                cursor=self.conexion.cursor()
                sql = "INSERT INTO cursos (codigo, nombre, duracion) VALUES ('{0}', '{1}', '{2}')"
                
               
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("curso registrado correctamente\n")
            except Error as ex:
                print("error al intentar registrar el curso: {0}".format(ex))


    def actualizarCurso(self,curso):
        if(self.conexion.is_connected()):
            try:
                cursor=self.conexion.cursor()
                sql = "UPDATE cursos SET nombre='{0}', duracion='{1}' WHERE codigo='{2}'"
                
               
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("curso actualizado correctamente\n")
            except Error as ex:
                print("error al intentar actualizar el curso: {0}".format(ex))

    def eliminarCurso(self,codigoCurso):

        if(self.conexion.is_connected()):
            try:
                cursor=self.conexion.cursor()
                sql = "DELETE FROM  cursos WHERE codigo='{0}'"
                
                cursor.execute(sql.format(codigoCurso))
                self.conexion.commit()
                print("curso eliminado correctamente\n")
            except Error as ex:
                print("error al intentar eliminado el curso: {0}".format(ex))