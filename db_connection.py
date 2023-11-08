import pymongo

def connect_to_mongodb():
    client = pymongo.MongoClient("mongodbURL") # replace mongodbURL with your Mongo DB URL
    return client["yourDatabase"] # replace yourDatabase with your Database Name
