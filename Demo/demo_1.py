# Imports 
from pymongo import MongoClient

# initialize a client, connect to database, Specify collection if already exists

client = MongoClient('localhost', 27017)
db = client['test_company']

######### Create
# Scenario - Create single document

# document = {"name" : "Ashish", "address" : "Pune" , "phone" : 1234567890 , "email_id": "ashish@test_company.com" , "department": "IT"}
# document = {"name" : "Abhishek", "address" : "Nagpur" , "phone" : 1223232435 , "email_id": "abhishek@test_company.com" , "department": "Accounts"}
# db.employee_col.insert_one(document)


# Scenario -  Create multiple documents using insert_many()

# documents = [{"name" : "Ashish", "address" : "Pune" , "phone" : 1234567890 , "email_id": "ankit@test_company.com" , "department": "Sales"},
#              {"name" : "Avinash", "address" : "Mumbai" , "phone" : 1325465768 , "email_id": "avinash@test_company.com" , "department": "Sales"},
#              {"name" : "Sheetal", "address" : "Delhi" , "phone" : 1322454567 , "email_id": "sheetal@test_company.com" , "department": "Admin"},
#              {"name" : "Kiran", "address" : "Mumbai" , "phone" : 1544365768 , "email_id": "kiran@test_company.com" , "department": "HR"},
#              {"name" : "Neha", "address" : "Banglore" , "phone" : 1233423345 , "email_id": "neha@test_company.com" , "department": "HR"}]
# db.employee_col.insert_many(documents) 


######### Read
# Scenario - Read single document
# filter = {}
# print(db.employee_col.find_one(filter))

# Scenario -  Read all documents
# filter = {}
# cursor = db.employee_col.find(filter)
# for document in cursor:
#     print(document)

# Scenario -  Read specific document - All employees in "Accounts" department 

# filter = {"department" : "Accounts"}
# cursor = db.employee_col.find(filter)
# for document in cursor:
#     print(document)



######### Update - change the department name from Admin to Accounts 

# Scenario - update many document using update_many()

# filter = {"department": "Admin"}
# update = {"$set" : {"department":"Accounts"}}
# db.employee_col.update_many(filter=filter,update=update,upsert=False)

# validate if update is successfull
# filter = {"department": "Accounts"}
# cursor = db.employee_col.find(filter)
# for document in cursor:
#     print(document)

# Scenario - update single document with update_one()

# filter = {"email_id" : "ankit@test_company.com"}
# update = {"$set" : {"name" : "Ankit"}}
# db.employee_col.update_one(filter,update, upsert=False)

# validate
# filter = {"email_id" : "ankit@test_company.com"}
# cursor = db.employee_col.find(filter)
# for document in cursor:
#     print(document)


######### Delete

# Scenario - Delete single document with email_id - ankit@test_company.com

# filter = {"email_id" : "ankit@test_company.com"}
# db.employee_col.delete_one(filter)

# Scenario - Delete multiple document with department - HR

# filter = {"department" : "HR"}
# db.employee_col.delete_many(filter)


# Scenario - Delete all documents from collection
# filter = {}
# db.employee_col.delete_many(filter)


# Scenario - Delete a colleciton 
# db.employee_col.delete_one(filter)

# Scenario - Delete database
# client.drop_database("employee_col") 