import os,csv
os.system("cls")
print("\n\n\t\t----BIENVENIDO AL PROGRAMA----\n\n")
running=True
database=[]
with open('DB.csv') as data:
    reader = csv.reader(data)
    for line in reader:
        database.append(line)

def show_menu():
    print("1-Cargar paciente\n2-Buscar paciente por nombre\n3-Listar pacientes\n4-Actualizar historial de paciente\n5-Salir del programa")
    action=input("Elija la opcion que desee: ")
    os.system("cls")
    return action

def validate_response(n):
    validate=False
    num_res=0

    if n.isdigit():
        num_res=int(n)
        if num_res >0 and num_res < 6:
            msg="en rango"
            validate=True
        else:
            msg="fuera de rango"
    else:
        msg="no es numero"
    return validate,num_res,msg

def carga_paciente(database):
    name=input("Ingrese el nombre: ")
    age=int(input("Ingrese la edad: "))
    history=input("Ingrese la historia clinica: ")
    paciente =[name,age,history]
    return paciente
    


def buscar_paciente(database,name):
    encontrado=False
    nombre=""
    info=[]
    index=0
    for i in range(len(database)):
        if database[i][0].lower()==name.lower():
            nombre = name
            info=database[i]
            index=i
            encontrado=True
    return nombre,info,encontrado,index

while running:
    response = show_menu()
    validate,num_res,msg=validate_response(response)
    if validate:
        if num_res==1:
            paciente=carga_paciente(database)
            database.append(paciente)
            print(database)
            print("\t\t----Paciente agregado----")
        elif num_res==2:
            os.system("cls")
            name=input("Ingrese el nombre del paciente que desea buscar: ")
            nombre,info,encontrado,index=buscar_paciente(database,name)
            if encontrado:
                print("Aqui tiene la informacion de ",nombre,"\n","Edad:", info[1],"\n","Historial:",info[2],"\n")
            else:
                print("\n\n----Paciente no encontrado----\n\n")
        elif num_res==3:
            os.system("cls")
            for i in range(len(database)):
                print("\n Nombre: ", database[i][0],"\n","Edad: ", database[i][1],"\n","Historial: ",database[i][2],"\n\n--------------------------\n")
        elif num_res==4:
            os.system('cls')
            name=input("Ingrese el nombre del paciente que desea buscar: ")
            nombre,info,encontrado,index=buscar_paciente(database,name)
            if encontrado:
                new_historial=input("Historial nuevo: ")
                historial=str(info[2])+"|"+new_historial
                print(historial)
                paciente=[nombre,info[1],historial]
                database.insert(index,paciente)
                database.pop(index+1)
                
            else:
                print("\n\n----Paciente no encontrado----\n\n")

        else:
            with open("DB.csv",'w',newline='') as db:
                write=csv.writer(db)
                for i in range(len(database)):
                    write.writerow(database[i])
            running=False
    else:
        print("\n\n---Opcion incorrecta---\n\n")
