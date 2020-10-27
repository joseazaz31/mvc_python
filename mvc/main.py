from controller.personacontroller import personacontroller

lista=["maria","flores","8089685","F","874",2]
enlace=personacontroller()
enlace.crearRegistro(lista)
listaRegistros=enlace.listarRegistros()#se obtiene los registros
print(listaRegistros)
for i in range(len(listaRegistros)):
    print("codigo: ",listaRegistros[i][0])
    print("nombre: ",listaRegistros[i][1])
    print("apellido: ",listaRegistros[i][2])
    print("Dni: ",listaRegistros[i][3])
    print("sexo: ",listaRegistros[i][4])
    print("ciclo: ",listaRegistros[i][5])
    print("********************")