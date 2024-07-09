import pandas as pd
import json

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://yoursamit01:2024amit@cluster0.mrqmjvn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Create database name and collection name
DATABASE_NAME="mydatabase"
COLLECTION_NAME="waferfault"

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# read the data
df = pd.read_csv(r'C:\my_project_pw\sensorFalultDetection\notebook\data\wafer_23012020_041211.csv')
df =df.drop('Unnamed: 0',axis=1)

json_record = list(json.loads(df.T.to_json()).values())

collection.insert_many(json_record)


