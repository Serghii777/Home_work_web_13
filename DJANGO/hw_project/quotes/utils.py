import certifi
from pymongo import MongoClient


uri = "mongodb+srv://user19:456123@clusterdbgoit.xlgrzju.mongodb.net/work10?retryWrites=true&w=majority"

def get_mongodb():
    client = MongoClient(uri, ssl=True, tlsCAFile=certifi.where())

    db = client["work10"]
    return db
