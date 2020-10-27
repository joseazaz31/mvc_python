from .Persona import Persona
from .conexion import conexion

class Alumno(Persona):
    codigo=""
    ciclo=""


    def __init__(self):
        pass


    def setDatosPersonales(self,nombres,apellido,dni,sexo):
        Persona.__init__(self,nombres,apellido,dni,sexo)

    def setMatricula(self,codigo,ciclo):
        self.codigo=codigo
        self.ciclo=ciclo

    def setCodigo(self,codigo):
        self.codigo=codigo

    def setCiclo(self,ciclo):
        self.ciclo=ciclo

    def getCiclo(self):
        return  self.ciclo

    def getCodigo(self):
        return  self.codigo
#*******************************************************
    def insertarAlumno(self):
        conecta=conexion()
        conecta.conectar()
        SQL="INSERT INTO Alumno(codigo,nombres,apellido,dni,sexo,ciclo) ""VALUES('"+self.codigo+"','"+self.nombres+"','"+self.apellido+"','"+self.dni+"','"+self.sexo+"',"+str(self.ciclo)+")"
        print(SQL)
        resp=conecta.setEjecutarQuery(SQL)
        if (resp):
            return 1
            #print("registro correcto")

        else:
            return 0
            #print("registro incorrecto")
#******************************************************
    def mostrarAlumno(self):
        conecta=conexion()
        conecta.conectar()
        SQL="SELECT *FROM alumno"
        registros=conecta.getEjecutarQuery(SQL)
        return registros

# ************************************************
    def actualizarAlumno(self,codigo):
        pass
    def eliminarAlumno(self,codigo):
        pass