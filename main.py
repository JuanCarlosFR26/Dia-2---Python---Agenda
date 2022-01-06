agenda = {}

def añadirContacto():
    nuevoContacto = agenda.setdefault(input('Nuevo Contacto'), input('Numero de contacto'))

añadirContacto()
añadirContacto()
añadirContacto()



def buscarContacto():
    cadena = input("Nombre del contacto que quieres buscar")
    for nombre, value in agenda.items():
        if nombre.startswith(cadena):
            print("El número de teléfono de %s es el %s" % (nombre, agenda[nombre]))



buscarContacto()


