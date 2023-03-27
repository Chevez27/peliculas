import pymongo

client = pymongo.MongoClient("mongodb+srv://henry19:Rusalem1@mongodb101.blt4rxb.mongodb.net/test")
db = client["Peliculas"]
collection = db["Registro"]