def buscval (list,target):
    for item in list:
        if item == target:
            return item
    return None
def quick_sort_Nombre(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]["Nombre"] < pivote[1]["Nombre"]]
    iguales = [x for x in lista if x[1]["Nombre"] == pivote[1]["Nombre"]]
    mayores = [x for x in lista[1:] if x[1]["Nombre"] > pivote[1]["Nombre"]]

    return quick_sort_Nombre(menores) + iguales + quick_sort_Nombre(mayores)

def quick_sort_Edad(lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]["Edad"] < pivote[1]["Edad"]]
        iguales = [x for x in lista if x[1]["Edad"] == pivote[1]["Edad"]]
        mayores = [x for x in lista[1:] if x[1]["Edad"] > pivote[1]["Edad"]]

        return quick_sort_Edad(menores) + iguales + quick_sort_Edad(mayores)
def ingresar_Participante(lista={}):
        dorsnum=int(input("ingrese numero de ID para el participante: "))
        name=input("ingrese nombre del participante: ")
        age=int(input("ingrese la edad del participante: "))
        if age > 10 and age < 101:
            if age >=10 and age <20:
                categ="Juvenil"
            elif age >=20 and age <50:
                categ="Adulto"
            elif age >=50:
                categ="Master"

            lista [dorsnum] = {
                "Nombre": name,
                "Edad": age,
                "Categ": categ
            }
        else:
            print("Ingreso invalido, intente nuevamente")
participantes={}
opt=0
while opt!=4:
    print("-----Menu Participantes------")
    print("1.Ingresar participante")
    print("2.Mostrar ordenados por Nombre")
    print("3.Mostrar ordenados por edad")
    print("Salir.")
    opt=int(input(""))
    match opt:
        case 1:
            ingresar_Participante(participantes)
        case 2:
            list = participantes.items()
            result = quick_sort_Nombre(list)
            for name, value in result:
                print(f"{value['Nombre']}, {value['Edad']}, {value['Categ']}")
        case 3:
            list = participantes.items()
            result = quick_sort_Edad(list)
            for name, value in result:
                print(f"{value['Nombre']}, {value['Edad']}, {value['Categ']}")

list= list(participantes.items())
result= quick_sort_Nombre(list)
for name, value in result:
    print(f"{value['Nombre']}, {value['Edad']}, {value['Categ']}")