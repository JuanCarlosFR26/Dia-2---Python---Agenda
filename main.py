agendaContactos = []
numeroContactos = []

def agregarContacto():
    contactoAdd = input('Introduzca nombre de contacto')
    numeroAdd = input('Número de contacto')
    agendaContactos.append(contactoAdd)
    numeroContactos.append(numeroAdd)
    print(agendaContactos)
    print(numeroContactos)

agregarContacto()
agregarContacto()


def buscarNumero():
    numeroAdd = input('Buscar número')
    for numero in numeroContactos:
        if numeroAdd in numeroContactos:
            print('El número localizado existe y es ', numero)
            break
        if numeroAdd not in numeroContactos:
            print('El número introducido no existe')
            break


buscarNumero()
