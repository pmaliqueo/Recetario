#Declaración de Librerías
from pathlib import Path
from os import system
import os

#Se realiza función de Bienvenida
def bienvenida():
    ruta = Path(Path.home(), "Recetas")
    print("Bienvenido al Recetario creado para ti\n")
    nombre = input("Dime tu nombre: ")
    system("clear")
    print(f"Hola {nombre}. La ruta donde se encuentran las recetas es: {ruta}")
    archivos = list(ruta.glob("*/*.txt"))
    cant_archivos = len(archivos)
    print(f"La cantidad de archivos en la ruta es: {cant_archivos}\n")
    return nombre, ruta

#Se realiza función de menu principal
def menu(nombre):
    principal = {"1":"Elegir Categoria", "2":"Crear Receta","3":"Crear Carpeta para Categoria","4":"Eliminar Receta","5":"Eliminar Categoria","6":"Finalizar Programa"}
    for num,opcion in principal.items():
        print(f"{num}-{opcion}")
    return principal


#Se realiza función de opcion1 para visualizar las Recetas
def opcion1():
    eleccion = input(f"\npor favor elije una de las opciones anteriores:")
    while eleccion != "6":
        if eleccion == "1":
            system("clear")
            elegir_categoria = os.listdir(ruta)
            valores = {}
            for indice, elemento in enumerate(elegir_categoria, start=1):
                clave = f"{indice}"
                valores[clave] = elemento
                print(f"{indice}: {elemento}")

            elegir_categoria = input("Elegir categoria: ")
            eleccion_de_categoria = os.path.join(ruta, elegir_categoria)
            if os.path.exists(eleccion_de_categoria):
                print("\nLas recetas para ver son las siguientes:  \n")
                for carne in Path(eleccion_de_categoria).glob("**/*.txt"):
                    print(carne.name)

                receta = input("\nEscribe la receta que deseas ver: ")
                ruta_receta = os.path.join(eleccion_de_categoria, receta)
                if os.path.isfile(ruta_receta):
                    nueva_receta = open(ruta_receta, "r")
                    print(nueva_receta.read())
                    nueva_receta.close()
                    volver = input("\nDeseas volver al menú? (Y/N): ")
                    if volver.upper() == "Y":
                        menu(nombre)
                        opcion1()
                        break
                    else:
                        print("Adios, Muchas Gracias por participar!")
                        break
                else:
                    print("Escribe el nombre correcto")
            else:
                print("Ingresa una opción válida")
        elif eleccion == "2":
            opcion2(eleccion)
            break
        elif eleccion == "3":
            opcion3(eleccion)
            break
        elif eleccion == "4":
            opcion4(eleccion)
            break
        elif eleccion == "5":
            opcion5(eleccion)
            break
    else:
        print("\nPrograma Terminado, Gracias por Participar")

    return eleccion

def opcion2(eleccion):
    while not eleccion == "6":
        if eleccion == "2":
            elegir_categoria = os.listdir(ruta)
            valores = {}
            for indice, elemento in enumerate(elegir_categoria, start=1):
                clave = f"{indice}"
                valores[clave] = elemento
                print(f"{indice}: {elemento}")
            elige_categoria = input("Elegir categoria: ")
            elige_categ = valores[elige_categoria]
            eleccion_de_categoria = os.path.join(ruta, elige_categ)
            if elige_categoria in valores:
                nombre_receta = input(f"Escribe el nombre de la nueva receta para la sección {valores[elige_categoria]}: ")
                contenido_receta = input("Escribe el contenido de la receta: ")
                receta_creada = os.path.join(eleccion_de_categoria, nombre_receta+".txt")
                nueva_receta = open(receta_creada,"a")
                nueva_receta.write(f"{contenido_receta}")
                nueva_receta.close()
                print(f"Nueva receta creada: {nombre_receta}")
                volver = input("\nDeseas volver al menú? (Y/N): ")
                if volver.upper() == "Y":
                    system("clear")
                    menu(nombre)
                    opcion1()
                    break
            else:
                print("Ingresa una opción válida")
        break

def opcion3(eleccion):
    nueva_categoria = input("Ingresa nombre de nueva Categoria: ")
    while not eleccion == "6":
        if eleccion == "3":
            nueva_carpeta = os.path.join(ruta,nueva_categoria)
            if os.path.exists(nueva_carpeta):
                print("Carpeta Existe")
            else:
                os.makedirs(nueva_carpeta)
                print(f"Nueva Categoria creada: {nueva_categoria}")
        volver = input("\nDeseas volver al menú? (Y/N): ")
        if volver.upper() == "Y":
            menu(nombre)
            opcion1()
            system("clear")
            break
        else:
            print("Adios, Muchas Gracias por participar!")
            break

def opcion4(eleccion):
    while eleccion != "6":
        if eleccion == "4":
            elegir_categoria = os.listdir(ruta)
            valores = {}
            for indice, elemento in enumerate(elegir_categoria, start=1):
                clave = f"{indice}"
                valores[clave] = elemento
                print(f"{indice}: {elemento}")

            eleccion_elimina = input("Elige Categoria para ver las recetas a eliminar: ")
            if eleccion_elimina in valores:
                elige_categ = valores[eleccion_elimina]
                categ = Path(ruta, elige_categ)
                print("\nLas recetas para ver son las siguientes:  \n")
                for elimina in Path(categ).glob("**/*.txt"):
                    print(elimina.name)

                delete = input("Elige la receta a eliminar: ")
                delete_ruta = os.path.join(categ, delete)
                print(delete_ruta)
                if os.path.exists(delete_ruta):
                    os.remove(delete_ruta)
                    print("Receta eliminada")
                else:
                    print("No se encuentra archivo")
                volver = input("\nDeseas volver al menú? (Y/N): ")
                if volver.upper() == "Y":
                    menu(nombre)
                    opcion1()
                    break
                else:
                    print("Adios, Muchas Gracias por participar!")
                    break
        break

def opcion5(eleccion):
    while not eleccion == "6":
        if eleccion == "5":
            elegir_categoria = os.listdir(ruta)
            valores = {}
            for indice, elemento in enumerate(elegir_categoria, start=1):
                clave = f"{indice}"
                valores[clave] = elemento
                print(f"{indice}: {elemento}")

            nueva_categoria = input("Ingresa nombre de la categoria a eliminar: ")
            nueva_carpeta = os.path.join(ruta, nueva_categoria)
            if os.path.exists(nueva_carpeta):
                os.rmdir(nueva_carpeta)
                print("Categoria Eliminada")
            else:
                print("No se encuentra Categoria")
        volver = input("\nDeseas volver al menú? (Y/N): ")
        if volver.upper() == "Y":
            menu(nombre)
            opcion1()
            system("clear")
            break
        else:
            print("Adios, Muchas Gracias por participar!")
            break




nombre, ruta = bienvenida()
menu(nombre)
opcion1()