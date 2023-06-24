from pymongo import MongoClient

# initialize a client, connect to database, Specify collection
client = MongoClient('localhost',27017)
db = client['my_store']
users_col = db['users']

# ##### Delete a single document 

# filter = {"name":"Akash"}
# delete_one_res = users_col.delete_one(filter)
# print(delete_one_res.acknowledged)
# print(delete_one_res.deleted_count)
# print(delete_one_res.raw_result)

# ##### Delete a multiple document
# filter = {}
# delete_many_res = users_col.delete_many(filter)
# print(delete_many_res.acknowledged)
# print(delete_many_res.deleted_count)
# print(delete_many_res.raw_result)


