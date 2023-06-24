## Imports
from pymongo import MongoClient

# initialize a client, connect to database, Specify collection
client = MongoClient('localhost', 27017)
db = client['my_store']

# #We will create a new collection named 'items'

# db.items.insert_many([
#     {"name": "Bag", "departments": ["School"], "versions": [
#         {"color": "Black", "size": "small", "qty": 5, "price": 17.79},
#         {"color": "Red", "size": "small", "qty": 3, "price": 18.23},
#         {"color": "Green", "size": "small", "qty": 5, "price": 20.03},
#         {"color": "Black", "size": "large", "qty": 1, "price": 41.23},
#         {"color": "Red", "size": "large", "qty": 10, "price": 46.82},
#         {"color": "Green", "size": "large", "qty": 7, "price": 45.43},
#     ]},
#     {"name": "Mug", "departments": ["Home", "Kitchen"], "versions": [
#         {"color": "White", "size": "11 oz", "qty": 14, "price": 14.79},
#         {"color": "Blue", "size": "11 oz", "qty": 23, "price": 15.23},
#         {"color": "Green", "size": "11 oz", "qty": 15, "price": 15.07},
#         {"color": "White", "size": "15 oz", "qty": 11, "price": 24.43},
#         {"color": "Blue", "size": "15 oz", "qty": 7, "price": 25.42},
#         {"color": "Green", "size": "15 oz", "qty": 10, "price": 25.83},
#     ]},
#     {"name": "Pens", "departments": ["School", "Office"], "versions": [
#         {"color": "Black", "type": "10 Pack", "qty": 40, "price": 14.79},
#         {"color": "Red", "type": "10 Pack", "qty": 13, "price": 15.23},
#         {"color": "Blue", "type": "10 Pack", "qty": 12, "price": 15.07}
#     ]}
# ])

# Helper function to print all entries in a cursor

def print_cursor(cursor):
    for document in cursor:
        print(document)

####### Searching for Data in Arrays

####### # Get all the documents in the collection that has "School" in departments field
# filter = {"departments":"School"}
# school_cursor = db.items.find(filter)
# print_cursor(school_cursor)

###### Get all the documents in the collection that has "Kitchen" in departments field
# filter = {"departments":"Kitchen"}
# school_cursor = db.items.find(filter)
# print_cursor(school_cursor)

####### Get all the documents in the collection that has exact array ['Home', 'Kitchen'] in departments field
# filter = {"departments":['Home', 'Kitchen']}
# school_cursor = db.items.find(filter)
# print_cursor(school_cursor)

## note - if you interchange the order in the array the match would not be found as shown below
# filter = {"departments":['Kitchen','Home']}
# school_cursor = db.items.find(filter)
# print_cursor(school_cursor)     # It will not return any matches

###### Getting entries based on the length of the array
## Get all the documents in the collection that has the departments array with size 2
# filter = {"departments": {"$size": 2}}
# length_cursor = db.items.find(filter)
# print_cursor(length_cursor) 


## Get all the documents in the collection that has the versions array with size 3
# filter = {"versions":{"$size":3}}
# length_cursor = db.items.find(filter)
# print_cursor(length_cursor)

### Important Note: You cannot do comparison with the size operator. Hence we can user the $where operator
# #The usage of $where operator involves Javascript code that gets the lenth attribute of the cesions array
# #Also its inefficient ways as it has to run custom JS code on corresponding entry within each document  

# filter = {"$where": "this.versions.length>3"} # in the backend the $where operator changes JS code to python code --> len(self.versions) > 3
# length_cursor = db.items.find(filter) 
# print_cursor(length_cursor)


###### Working with Arrays of Embedded documents

# # Get all the documents from the collection that has 'colour' field as 'Red'

# filter = {"versions.color": "Red"}
# version_colour_cursor = db.items.find(filter)
# print_cursor(version_colour_cursor)

# # We can check if the embedeed document has certain field(attribute) using $exists operator
# #Get all the documents that has the field "size"

# filter = {"versions.size" : {"$exists": True}}
# exists_cursor = db.items.find(filter)
# print_cursor(exists_cursor)
## To get all documents where size field does not exists set $exists operator to False

# filter = {"versions.size" : {"$exists": False}}
# exists_cursor = db.items.find(filter)
# print_cursor(exists_cursor)


# ###### We can also run comparison operators on embedded documents
# #Get all the documents with field version that has attribute 'qty' greater than 35

# filter = {"versions.qty":{"$gt": 35}}
# embeeded_cursor = db.items.find(filter)
# print_cursor(embeeded_cursor)


########### Updating Arrays in embedded documents


# filter = {"name":"Pens"}
# cursor = db.items.find_one(filter)
# print(cursor)

# Now updating the 'departments' field in the document with 'School'
# filter = {"name":"Pens"}
# update = {"$set": {"departments":["classroom"]}}
# db.items.update_many(filter,update)
# Verifying if the update is successful
# print(db.items.find_one(filter)['departments'])


#### Scenario - Remove the last element in departments field for document name 'Mug'

# check if document present 
# filter = {"name":"Mug"}
# print_cursor(db.items.find(filter))
# Update
# filter = {"name":"Mug"}
# update = {"$pop":{"departments":-1}} # removes last element from departments array. If the value is 1 then first element will be removed 
# db.items.update_many(filter,update)
# print_cursor(db.items.find(filter))

# You can specifically push the entry to arrays using $push operator
# filter = {"name":"Mug"}
# update = {"$push" : {"departments" : "Office"}}
# db.items.update_many(filter,update)
# # Validate
# print_cursor(db.items.find(filter))


# Add (trying some scenario)
# filter = {"name":"Mug"}
# update= {"$set":{"departments":["Home","Kitchen"]}}
# db.items.update_one(filter,update)
# print(db.items.find_one(filter))


##### $addToSet operator - addToSet operator is used to add elements to an array field within a MongoDB document if they do not already exist in the array. It ensures that duplicate values are not added to the array.
## Add a 'Technology' department to 'Mug' document only if it does not exists

# filter = {"name":"Mug"}
# update = {"$addToSet": {"departments": "Technology"}}
# db.items.update_one(filter,update)

