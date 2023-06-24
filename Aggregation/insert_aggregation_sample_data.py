from pymongo import MongoClient

LOCALHOST_URI = "mongodb://localhost:27017/"

def insert_data(mongo_uri=LOCALHOST_URI, db_name="aggregation_test", check_db_for_existing_entries=True):

    client = MongoClient(mongo_uri)
    db = client[db_name]

    if check_db_for_existing_entries:
        users_col_count = db.users.count_documents({})
        products_col_count = db.products.count_documents({})
        orders_col_count = db.orders.count_documents({})

        if users_col_count > 0 or products_col_count > 0 or orders_col_count > 0:
            print("Entries already exist in the {} database in the users, products, or orders collection. Insert commands aborted.".format(db_name))
            return None
        

    db.users.insert_many([
        {"name": "Sarah"},
        {"name": "Bob"},
        {"name": "Jose"},
        {"name": "Lisa"},
        {"name": "Jessica"},
        {"name": "Tina"}
    ])

    user_ids = db.users.find({}).distinct("_id")

    db.products.insert_many([
        {"name": "Mug", "seller_id": user_ids[0], "tags": ["Home", "Kitchen"]},
        {"name": "Moisturizer", "seller_id": user_ids[0], "tags": ["Beauty"]},
        {"name": "Pens", "seller_id": user_ids[1], "tags": ["Office", "School"]},
        {"name": "Face Cleanser", "seller_id": user_ids[0], "tags": ["Beauty"]},
        {"name": "Concealer Makeup", "seller_id": user_ids[3], "tags": ["Beauty"]},
        {"name": "Eyeliner", "seller_id": user_ids[4], "tags": ["Beauty"]}
    ])

    product_ids = db.products.find({}).distinct("_id")

    db.orders.insert_many([
        {"items": [{"product_id": product_ids[1], "quantity": 1}, {"product_id": product_ids[3], "quantity": 1}]},
        {"items": [{"product_id": product_ids[4], "quantity": 1}, {"product_id": product_ids[5], "quantity": 1}]},
        {"items": [{"product_id": product_ids[2], "quantity": 5}, {"product_id": product_ids[0], "quantity": 1}]},
        {"items": [{"product_id": product_ids[1], "quantity": 2}, {"product_id": product_ids[5], "quantity": 1}]},
        {"items": [{"product_id": product_ids[1], "quantity": 1}]},
        {"items": [{"product_id": product_ids[3], "quantity": 1}]},
    ])

    print("Done")


if __name__ == '__main__':
    insert_data()
    