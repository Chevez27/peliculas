from CRUD import *
from function_basic import *
while True:
    print("Menu de opciones")
    print("1. Ver todos las peliculas")
    print("2. Buscar un registro")
    print("3. Agregar un registro")
    print("4 Actualizar un registro")
    print("5 Eliminar un registro")


    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        show_movies()
    elif opcion == "2":
        nombre =(input("Ingrese nombre a buscar: "))
        show_movies_filters(nombre)
    elif opcion == "3":
        movie = create_json_movies()
        create_movie(movie)
    elif opcion == "4":
        nombre = (input("Ingrese el registro a modificar: "))
        movie = create_json_movie_update()
        update_movie(nombre, movie)
    elif opcion == "5":
        nombre = input("Ingresa el registro a eliminar")
        delete_movie(nombre)

