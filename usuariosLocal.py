import threading
#threading.local en el que cada hilo va a almacenar la sesion
datos_sesion= threading.local()

#Clase sesionUsuario, con su metodo para iniciar y mostrar la sesion
class SesionUsuario:
    def iniciar_sesion(self,nombre_usuario):
        datos_sesion.nombre = nombre_usuario

    def mostrar_sesion(self):
        print("Sesion iniciada para el usuario: " + datos_sesion.nombre)

#Funcion que va a ejecutar cada uno de los hilos, se crea y muestra una sesion con el usuario pasado como parametro
sesion= SesionUsuario()
def gestionar_sesion(nombre_usuario):
    sesion= SesionUsuario()
    sesion.iniciar_sesion(nombre_usuario)
    sesion.mostrar_sesion()

#Lista de usuarios, cada hilo va a tratar 1 usuario de la lista
listaUsuarios={"Ana", "Carlos", "Beatriz", "David", "Elena"}
#Los hilos inician la funcion gestionar_sesion, se pasa el nombre de usuario con args
hilos=[]
for usuario in listaUsuarios:
    hilo=threading.Thread(target=gestionar_sesion, args=(usuario,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()
print("Todos los hilos han terminado")






