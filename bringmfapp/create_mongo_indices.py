import pymongo
client = pymongo.MongoClient()
c = client['bring_my_food']
print c.users.create_index("email", unique=True)
print c.requests.create_index("table_id", unique=True)