# Imports
import pymongo
from pymongo import MongoClient

# initialize a client, connect to database, Specify collection
client = MongoClient('localhost' , 27017)
db = client.my_store
products_col = db.products # it will create a products collection if it doesn't exists while creating the document 

# Insert single data
# bag = {"name" : "Bag A" , "price" : 234}
# insert_one_res = products_col.insert_one(bag)  # it will return an instance of InsertOneResult class with attributes inserted_id, acknowledged
# insert_one_res = products_col.insert_one(bag)   # check the duplicate key scenario - For inserting multiple products you will get exception of pymongo.errors.DuplicateKeyError
# print(insert_one_res.acknowledged)
# print(insert_one_res.inserted_id)
# Docs - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html


# Insert multiple data - IMPORTANT (it will insert partial data even if insert many operations fails)
# phone = {"name" : "IPhone 11", "price" : 31000}
# laptop = {"name" : "HP Omen", "price" : 81000}
# insert_many_res = products_col.insert_many([phone,laptop]) # it will return an instance of InsertManyResult class with attributes inserted_ids, acknowledged
# insert_many_res = products_col.insert_many([phone,laptop]) # check the duplicate key scenario - For inserting multiple products you will get exception of pymongo.errors.BulkWriteError
# print(insert_many_res.acknowledged)
# print(insert_many_res.inserted_ids)
# Docs - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html




# Error Handling with try...except

# try:
#     # insert_one_res = products_col.insert_one(bag)  
#     # insert_one_res = products_col.insert_one(bag)  
#     insert_many_res = products_col.insert_many([phone,laptop]) 
#     insert_many_res = products_col.insert_many([phone,laptop]) 



# except pymongo.errors.DuplicateKeyError:
#     print("Duplicate key detected..while performing insert_one")

# except pymongo.errors.BulkWriteError:
#     print("Duplicate key detected..while performing insert_many")

