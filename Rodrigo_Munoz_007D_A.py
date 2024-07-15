import random
import csv

trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

def asignar_sueldos(trabajadores):
    return{trabajador:random.randint(300000,2500000) for trabajador in trabajadores}

def clasificar_sueldos(sueldos):
    total_sueldos=0
    print("Lista de empleados")
    for trabajador, sueldo in sueldos.items():
        total_sueldos+=sueldo
        if sueldo<800000:
            clasificacion="Sueldo menor a 800000"
        elif 800000<=sueldo<=2000000:
            clasificacion="Sueldo entre 800000 y 2000000"
        else:
            clasificacion="Sueldo superior a 6"
    print(f"Nombre:{trabajador}, Sueldo:{sueldo}, Clasificacion:{clasificacion}")
    print(f"Total de sueldos es:{total_sueldos}")
    
def mostrar_estadistica(sueldos):
    sueldos_lista=list(sueldos.values())
    sueldo_max=max(sueldos_lista)
    sueldo_min=min(sueldos_lista)
    promedio=sum(sueldos_lista)/len(sueldos_lista)

    print(f"Sueldo mas alto:{sueldo_max}")
    print(f"Sueldo mas bajo:{sueldo_min}")
    print(f"Promedio de sueldos:{promedio:.2f}")

def reporte_sueldos(sueldos):
    print("Reporte de sueldos")
    for trabajador, sueldo in sueldos.items():
        descuento_salud=sueldo*0.07
        descuento_afp=sueldo*0.12
        sueldo_liquido=sueldo - descuento_salud - descuento_afp
        print(f"Nombre:{trabajador},Sueldo base:{sueldo},Descuento salud:{descuento_salud},Descuento AFP:{descuento_afp},Sueldo liquido:{sueldo_liquido:.2f}")

def exportar_csv(sueldos):
    with open('reporte_sueldos.csv','w', newline='') as csvfile:
        fieldnames=['Nombre','Sueldo base','Descuento salud','Descuento AFP','Sueldo liquido']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for trabajador, sueldo in sueldos.items():
            descuento_salud=sueldo*0.07
            descuento_afp=sueldo*0.12
            sueldo_liquido=sueldo - descuento_salud - descuento_afp
            writer.writerow({'Nombre':trabajador, 'Sueldo base':sueldo,'Descuento salud':descuento_salud,'Descuento AFP':descuento_afp, 'Sueldo liquido':sueldo_liquido})
            print("Datos exportados con exito.")

def menu_principal():
    while True:
        print("Menu")
        print("1.- Asignar sueldo aleatorio")
        print("2.- Clasificar sueldo")
        print("3.- Ver estadistica")
        print("4.- Reporte de sueldos")
        print("5.- Exportar a csv")
        print("6.- Salir")
        opcion=int(input("Seleccione una opcion:"))
        if opcion==1:
            asignar_sueldos(sueldos)
        elif opcion==2:
            clasificar_sueldos(sueldos)
        elif opcion==3:
            mostrar_estadistica(sueldos)
        elif opcion==4:
            reporte_sueldos(sueldos)
        elif opcion==5:
            exportar_csv(sueldos)
        elif opcion==6:
            print("Finalizando programa...")
            print("Desarrollado por Rodrigo Munoz")
            print("Rut 18.811.653-1")
            break
        else:
            print("Opcion no valida")

if __name__=="__main__":
    menu_principal()