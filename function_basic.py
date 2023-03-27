def create_json_movies():
    nombre = input ("Nombre")
    categoria= input ("Categoria")
    fecha = input ("Fecha de emision")

    movie= {
        "nombre": nombre,
        "categoria": categoria,
        "fecha" : fecha}
    return movie


def create_json_movie_update():
    print("Menu de opciones")
    print("1. Modificar todo el documento")
    print("2. Moficar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        return create_json_movies()
    elif opcion == "2":
        indice = input("Ingrese el indice a buscar: ")
        valor = input("Ingrese el valor a sustituir: ")
        movie ={indice:valor}
    return movie

