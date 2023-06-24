from pymongo import MongoClient

# initialize a client, connect to database, Specify collection
client = MongoClient("localhost", 27017)
db = client['my_store']
products_col = db['products']

#   ####### update_one() - Update a single document
# # Modify price for apple watch
# update_one_res = products_col.update_one({"name":"Apple watch"}, {"$set": {"price": 21}})
# # print(update_one_res)
# print(update_one_res.acknowledged)
# print(update_one_res.matched_count)
# print(update_one_res.modified_count)
# print(update_one_res.upserted_id)


# ######## replace_one() - update a single document in a collection by completely replacing it with a new document
# #Docs - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.replace_one
# #replace apple watch document to include seller and field name as product_name
# filter = {"name": "Apple watch"}
# replacement = {"product_name": "Apple New Watch", "price": 25, "seller": "Apple INC"}
# replace_one_res = products_col.replace_one(filter,replacement=replacement,upsert=False)
# print(replace_one_res.acknowledged)
# print(replace_one_res.matched_count)
# print(replace_one_res.modified_count)
# print(replace_one_res.upserted_id)

# ######## update_many() -  allows you to modify multiple documents simultaneously with a single operation
# #update all documents with name Iphone 11 with a new price

# filter = {"name": "IPhone 11"}
# update = {"$set":{"price": 41000}}

# update_many_res = products_col.update_many(filter,update,upsert=False)
# print(update_many_res.acknowledged)
# print(update_many_res.matched_count)
# print(update_many_res.modified_count)
# print(update_many_res.upserted_id)

# ######## upsert - refers to the concept of updating a document if it exists in the collection, or inserting a new document if it doesn't exist.
# # the document with the name 'Hat' initially does not exists. We will enable the upsert functionality to create a new document with nama Hat 
# filter = {"name":"Hat"}
# update = {"$set": {"name":"Hat", "price": 550}}
# update_upsert_res = products_col.update_many(filter,update,upsert=True)
# print(update_upsert_res.acknowledged)
# print(update_upsert_res.matched_count)
# print(update_upsert_res.modified_count)
# print(update_upsert_res.upserted_id)

# ####### Update Operators - 
# #Docs - https://www.mongodb.com/docs/manual/reference/operator/update/

# ### $currentDate - Sets the value of a field to current date, either as a Date or a Timestamp.
# filter = {}
# update = {"$currentDate":{"date":True}}

# products_col.update_many(filter, update)

# ### $rename - Renames a field.
# filter = {}
# update = {"$rename" : {"date" : "date_added"}}
# products_col.update_many(filter,update)

# ### $mul - Multiplies the value of the field by the specified amount.
# filter = {}
# update = {"$mul": {"price":0.5}}
# products_col.update_many(filter, update)

# ### $unset - Removes the specified field from a document.
# filter = {}
# update = {"$unset":{"date_added": True}}
# products_col.update_many(filter,update)
