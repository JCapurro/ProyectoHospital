import os
os.system("cls")
print("\n\n\t\t----BIENVENIDO AL PROGRAMA----\n\n")
running=True
database=[{'Nombre': 'Juan', 'Edad': 18, 'Historial': 'asdasd'}, {'Nombre': 'Pepe', 'Edad': 54, 'Historial': 'Pedos'}, {'Nombre': 'Pablo', 'Edad': 44, 'Historial': 'Caca'}]

def show_menu():
    print("1-Cargar paciente\n2-Buscar paciente por nombre\n3-Listar pacientes\n4-Salir del programa")
    action=input("Elija la opcion que desee: ")
    os.system("cls")
    return action

def validate_response(n):
    validate=False
    num_res=0

    if n.isdigit():
        num_res=int(n)
        if num_res >0 and num_res < 5:
            msg="en rango"
            validate=True
        else:
            msg="fuera de rango"
    else:
        msg="no es numero"
    return validate,num_res,msg

def carga_paciente():
    name=input("Ingrese el nombre: ")
    age=int(input("Ingrese la edad: "))
    history=input("Ingrese la historia clinica: ")
    paciente={'Nombre': name,'Edad':age,'Historial':history}
    return paciente

def buscar_paciente(database,name):
    encontrado=False
    nombre=""
    info={}
    for i in range(len(database)):
            if database[i]["Nombre"].lower()==name.lower():
                nombre = name
                info=database[i]
                encontrado=True
    return nombre,info,encontrado

#def listar_paciente(database):


while running:
    response = show_menu()
    validate,num_res,msg=validate_response(response)
    if validate:
        if num_res==1:
            paciente=carga_paciente()
            database.append(paciente)
            print("\t\t----Paciente agregado----")
        elif num_res==2:
            os.system("cls")
            name=input("Ingrese el nombre del paciente que desea buscar: ")
            nombre,info,encontrado=buscar_paciente(database,name)
            if encontrado:
                print("Aqui tiene la informacion de ",nombre,"\n","Edad:", info["Edad"],"\n","Historial:",info["Historial"],"\n")
            else:
                print("\n\n----Paciente no encontrado----\n\n")
        elif num_res==3:
            os.system("cls")
            for i in range(len(database)):
                print("\n Nombre: ", database[i]["Nombre"],"\n","Edad: ", database[i]["Edad"],"\n","Historial: ",database[i]["Historial"],"\n\n--------------------------\n")
        else:
            running=False
    else:
        print("\n\n---Opcion incorrecta---\n\n")
