# Imports
from pymongo import MongoClient
from insert_aggregation_sample_data import insert_data

client = MongoClient('localhost', 27017)
db = client['aggregation_test']

# Helper Function
def print_cursor(cursor):
    for document in cursor:
        print(document, end='\n\n')

insert_data("mongodb://localhost:27017","aggregation_test")


############# $match - Filters the documents to pass only the documents that match the specified condition(s) to the next pipeline stage.

# match_cursor = db.products.aggregate([
#     {"$match": {"name":"Pens"}}                          # Stage
# ])
# print(match_cursor) # Return an instance of ComandCursor class
# print_cursor(match_cursor)

# Functionality of $match operator Simillar to find method with a filter
# filter = {"name":"Pens"}
# pens_cursor = db.products.find(filter)
# print_cursor(pens_cursor)


# Scenario - get all documents that match the tags of Beauty or Home
# pipeline = [{"$match" : {"$or":[{"tags":"Home"},{"tags":"Beauty"}]}}]
# cursor = db.products.aggregate(pipeline)
# print_cursor(cursor)


############# $project - takes a document that can specify the inclusion of fields, the suppression of the _id field, the addition of new fields, and the resetting of the values of existing fields.
#  Alternatively, you may specify the exclusion of fields.
# pipeline_0 = [{"$project" : {"_id" : 0}}]             # 0 - exclude field
# pipeline_1 = [{"$project" : {"_id" : 0, "tags":1}}]     # 1- include field
# pipeline = [{"$project" : {"_id" : 0, "product_name" : "$name", "tags": 1}}] # modify existing field name 'name' by 'product_name'
# command_cursor = db.products.aggregate(pipeline)
# print_cursor(command_cursor)

############# 2-Stage Aggregation Pipeline Implementation using $match and $project

# pipeline = [{"$match" : {"name" : "Pens"}},
#             {"$project" : {"product_name" : "$name" , "tags" : 1, "_id" : 0}}]

# command_cursor = db.products.aggregate(pipeline)
# print_cursor(command_cursor)


############# $unset - Removes/excludes fields from documents

# pipeline = [{"$unset" : "_id"}]
# command_cursor = db.products.aggregate(pipeline)
# print_cursor(command_cursor)

# Implementing 2-stage pipeline with $match and $unset
# pipeline = [{"$match" : {"name" : "Pens"}},
#             {"$unset" : "_id"}]
# command_cursor = db.products.aggregate(pipeline)
# print_cursor(command_cursor)