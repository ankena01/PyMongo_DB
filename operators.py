import pymongo
from pymongo import MongoClient

# initialize a client, connect to database, Specify collection

client = MongoClient('localhost',27017)
db = client['my_store']
products_col = db['products']


# Helper function to print all entries in a cursor

def print_cursor(cursor):
    for document in cursor:
        print(document)

### print all documents in collection
# print_cursor(products_col.find())


# ###### Comparison Operators - $lt (Less Than)

# lt_cursor = products_col.find({"price": {"$lt":31000}})
# print_cursor(lt_cursor)
# print('\n')

# ## combining with other operator $gte - Greater Than or Equal to
# lt_gte_cursor = products_col.find({"price" : {"$lt" : 31000, "$gte":234}})
# print_cursor(lt_gte_cursor)

### Applying operators on multiple attributes at same time
## Get all documents that are less than 31000 but not "Apple watch"
# lt_ne_cursor = products_col.find({"price": {"$lt": 31000} , "name" : {"$ne": "Apple watch"}}) 
# print_cursor(lt_ne_cursor)

# ###### Logical Operators - $and opertaor
### Get all documents that are less than 31000 and exclude "Apple watch"

# and_cursor = products_col.find({"$and" : [
#                             {"price": {"$lt": 31000}},
#                             {"name": {"$ne":"Apple watch"}}
#                             ]})
# print_cursor(and_cursor)

# ###### Logical Operators - $or operator
#### Exclude apple watch document
 

# or_cursor = products_col.find({"$or":[
#                                       {"price" : {"$lt": 19}},
#                                       {"price": {"$gt": 21}}      
# ]})
# print_cursor(or_cursor)

# ###### Logical Operators - $nor operator
#### Get all documents with Apple watch

# nor_cursor = products_col.find({"$nor" : [
#                                         {"price": {"$lt": 19}},
#                                         {"price": {"$gt": 21}},
# ]

# })

# print_cursor(nor_cursor)

# ###### $type Operator - Identify the datatype of data

# type_cursor = products_col.find({"price": {"$type": "double"}})
# print_cursor(type_cursor)

# ###### $exists - check if specific attribute exists

# exists_cusrsor = products_col.find({"seller": {"$exists":True}})
# print_cursor(exists_cusrsor)

# ###### $regex - search for substringwithin the query entries

# #case sensetive 
# regex_cursor = products_col.find({"name": {"$regex": "Apple"}})
# print_cursor(regex_cursor)

# #case insensetive

# regex_cursor_options = products_col.find({"name": {"$regex": "apple", "$options": "i"}})
# print_cursor(regex_cursor_options)