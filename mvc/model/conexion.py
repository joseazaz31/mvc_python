import pymysql

class conexion:
    def __init__(self):
        self.servidores="localhost"
        self.bd="senati_bd"
        self.user="root"
        self.clave=""

    def conectar(self):
        try:
            self.conexion=pymysql.connect(self.servidores,self.user,self.clave,self.bd)
            self.cn=self.conexion.cursor()
            print("se conecto a la base de datos")
        except exception as e:
            print("error: ",e)
    def setEjecutarQuery(self,sql):
        try:
            respuesta=self.cn.execute(sql)
            print("respuesta -->: ",respuesta)
            self.conexion.commit()
            self.conexion.close()
            return 1

        except Exception as ex:
            print("error: ",ex)
            self.conexion.rollback()
            return 0
        #select
    def getEjecutarQuery(self,sql):
        try:
            self.cn.execute(sql)
            registros=self.cn.fetchall()
            return registros

        except Exception as ex:
            print("error:",ex)
            return 0