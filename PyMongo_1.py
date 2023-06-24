from pymongo import MongoClient

######### Initialize a client to connect to MongoDB

# Method 1
# client = MongoClient('localhost',27017)

# Method 2
client = MongoClient("mongodb://localhost:27017")
# print(client)

######## Show the existing databases - Alternatively you can use MongoSH or Compass
# print(client.list_database_names()) 

######### connect to a datbase named my_store. This is simillar to CLI command - use <databasename> 

# Method 1
db = client['my_store']

# Method 2
# db = client.my_store
# print(db)


######## Show the collections within the database
# print(db.list_collection_names())


######### Access a specific collection within the database

# Method1
# users_col = db.users

# Method 2
users_col = db['users']
# print(users_col)

######### Create document 

# users_col.insert_one({"name":"Amreesh","age":29})

########## Read the document - Find a single object based on a filter
# print(users_col.find_one({"name":"Amreesh"}))

########## Update a single document
# users_col.update_one({"name":"Amreesh"}, {"$set":{"name" : "Sachin", "age": 20}})

########## Delete a single document
# users_col.delete_one({"name": "Amreesh"})

########## Delete all documents
users_col.delete_many({})
