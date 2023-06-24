# Imports
import pymongo
from pymongo import MongoClient
import math

# initialize a client, connect to database, Specify collection
client = MongoClient('localhost', 27017)
db = client.my_store
products_col = db.products

######## find_one() - retrive a single entry from database with the matching value
# by default it will return the first matched data from the collection
# print(products_col.find_one({ "name" : "IPhone 11" }))

######## find() and cursor object
# print(products_col.find({ "name" : "IPhone 11" })) # Returns a pymongo.cursor.Cursor object

# In PyMongo, a cursor is an object that is used to iterate over the results of a MongoDB query
# cursor object points to a location in query result rather than loading the entire query result in memory

# phone_cursor = products_col.find({ "name" : "IPhone 11" })

# for document in phone_cursor:
#     print(document)

# print(phone_cursor.alive) #The alive attribute in PyMongo is a boolean value that indicates whether the cursor has the potential to return more data

########## Significance of cursor object

# while phone_cursor.alive:
#     document = phone_cursor.next()
#     print(document)

########## sort() - in Ascending - Instead of pymongo.ASCENDING you can use 1

# cursor = products_col.find({})
# for document in cursor.sort("price",pymongo.ASCENDING):
#     print(document)
    
########## sort() - in Descending - Instead of pymongo.DESCENDING you can use -1

# cursor = products_col.find()
# for document in cursor.sort("price",pymongo.DESCENDING):
#     print(document)

########## sort() - Sort on the basis of multiple keys

# cursor = products_col.find()
# for document in cursor.sort([("price",pymongo.DESCENDING),("name",pymongo.DESCENDING)]):
#     print(document)

########## limit() and skip() functionality on the cursor object

# cursor = products_col.find()
# for document in cursor.limit(3):
#     print(document)

##########  combining the functionality of limit and descending sort
# cursor = products_col.find()
# for document in (cursor.sort([("price",-1),("name",-1)])).limit(7):
#     print(document)


########## skip() method
# cursor = products_col.find()
# for document in cursor.skip(7):
#     print(document)



########## Senario - Display 5 products per page on ecommerce website
# print(products_col.count_documents({})) # display total count of documents in collection


# page_item_limit = 5         # Max 5 items to be displayed per page
# total_pages = products_col.count_documents({}) / page_item_limit
# total_pages = math.ceil(total_pages) # total pages requireed to display all documents
# # print(total_pages)


# for page_num in range(1, total_pages+1):
#     print(f"--Page {page_num}--")
#     cursor = products_col.find()
#     for document in cursor.skip((page_num-1)*page_item_limit).limit(page_item_limit).sort("price",1):
#         print(document)


######### count_documents() - count the documents for a specific type 
# find all iphone related documents
# print(products_col.count_documents({"name":"IPhone 11"}))
# print(products_col.estimated_document_count())

######### distinct() - Useful for finding unique data in the colection. Also helpful in finding duplicate entries by paring with count_documents() method
# cursor = products_col.find()
# print(cursor.distinct("name"))

# Scenario - Find duplicate entries vs unique entries in collection
# cursor = products_col.find()
# unique_names = len(cursor.distinct("name"))
# total_documents = products_col.count_documents({})
# print(f"There are {unique_names} unique products vs {total_documents-unique_names} duplicates")

######### Projection functinality -  projection refers to the process of specifying which fields to include or exclude from the query results

# projection = {"name" : 1, "_id" : 0}
# cursor = products_col.find({}, projection)

# for document in cursor:
#     print(document)

# By default id key will be retrived unless you explicitly exclude in projection