from model.Alumno import Alumno
class personacontroller:

    def __init__(self):
        pass

    #**********crear registro*********#
    def crearRegistro(self,lista):
        self.enlace=Alumno()
        self.enlace.setDatosPersonales(lista[0],lista[1],lista[2],lista[3])
        self.enlace.setMatricula(lista[4],lista[5])
        resp=self.enlace.insertarAlumno()
        if (resp):
            print("registro correcto")
        else:
            print("registro incorrecto")


    #***********leer registro**********#
    def listarRegistros(self):
        self.enlace=Alumno()
        lista=self.enlace.mostrarAlumno()
        return lista

        pass
    #***********actualizar registro****#
    def actualizarRegistro(self):
        pass
    #*********eliminar registro********#
    def eliminarRegistro(self):
        pass