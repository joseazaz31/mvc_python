class Persona:

    def __init__(self, nombres, apellido, dni, sexo):
        self.nombres = nombres
        self.apellido = apellido
        self.dni = dni
        self.sexo = sexo

    def setNombres(self, nombres):
        self.nombres = nombres

    def setApellido(self, apellido):
        self.apellido = apellido

    def setDni(self, dni):
        self.dni = dni

    def setsexo(self, sexo):
        self.sexo = sexo

    def getNombres(self):
        return self.nombres

    def getApellido(self):
        return self.apellido

    def getDni(self):
        return self.dni

    def getSexo(self):
        return self.sexo