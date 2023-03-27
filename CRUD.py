from parameters import collection


def show_movies(id= None):
    if id is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        query = {"_id": id}
        document = collection.find_one(query)
        print(document)
def show_movies_filters(nombre):
    if nombre == nombre:
        documents = collection.find_one(nombre)
        print(documents)
    else:
        document = collection.find_one()
        print(document)



def create_movie(movie):
    result = collection.insert_one(movie)
    print(result.inserted_id)


def update_movie(nombre, json_update):
    query = {"nombre": nombre}
    new_values = {"$set": json_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)

def delete_movie(nombre):

    resultado = collection.delete_one(filter)
    return resultado.deleted_count


