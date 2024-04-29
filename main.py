import pymongo

# Provide the mongodb localhost url to connect python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/neurolab")

# Database Name
database = client['neurolab']

# Collection Name
collection = database['Products']

# sample data
d = {'companyName':'Google',
     'product':'Gemini',
     'productType': 'LLM'}

# Insert Above record in the collection
rec = collection.insert_one(d)

# Lets verify all the record at once present in the collection
all_record = collection.find()

# printing all records present in the collection
for idx, record in enumerate(all_record):
    print(f"{idx}: {record}")