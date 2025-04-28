from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime, timezone



mongo_client = "mongodb://localhost:27017/paperless_dcs"

try:
    client = MongoClient(mongo_client)

    db = client.get_database("paperless_dcs")

    collections = db.list_collection_names()

    # Print the collection names
    print(f"{collections} Collections in the database:")

    # Check if the connection is successful
    print("MongoDB connection successful")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")




# Connect to MongoDB
db = client.get_database('paperless_dcs')
users = db['users']

# Clear existing users (optional for reset)
# users.delete_many({})

# Predefined office-based users
user_data = [
    {
        "username": "Director",
        "email": "dcs.director@dsa.mil.ng",
        "password": "director123",
        "role": "director",
        "office": "DCS Director's Office"
    },
    {
        "username": "Registry",
        "email": "dcs.registry@dsa.mil.ng",
        "password": "registry123",
        "role": "registry",
        "office": "DCS Registry Unit"
    },
    {
        "username": "DD ComSat",
        "email": "dd.comsat@dsa.mil.ng",
        "password": "comsat123",
        "role": "officer",
        "office": "DD ComSat Office",
        "unit": "ComSat Division"
    },
    {
        "username": "DD ICT",
        "email": "dd.ict@dsa.mil.ng",
        "password": "ict123",
        "role": "officer",
        "office": "DD ICT",
        "unit": "ICT Division"
    },
    {
        "username": "DD Strat App/Net",
        "email": "dd.stratapp@dsa.mil.ng",
        "password": "strat123",
        "role": "officer",
        "office": "DD Strat App/Net Ops",
        "unit": "Strat App Division"
    },
    {
        "username": "AD ComSat",
        "email": "ad.comsat@dsa.mil.ng",
        "password": "adcomsat123",
        "role": "officer",
        "office": "AD ComSat",
        "unit": "ComSat Division"
    },
    {
        "username": "AD ICT",
        "email": "ad.ict@dsa.mil.ng",
        "password": "adict123",
        "role": "officer",
        "office": "AD ICT",
        "unit": "ICT Division"
    },
    {
        "username": "AD Strat App/Net",
        "email": "ad.stratapp@dsa.mil.ng",
        "password": "adstrat123",
        "role": "officer",
        "office": "AD Strat App/Net",
        "unit": "Strat App Division"
    }
]



# Insert users with hashed passwords
for user in user_data:
    user['password'] = generate_password_hash(user['password'])
    user['created_at'] = datetime.now(timezone.utc)

    # Avoid duplicate usernames
    existing = users.find_one({"email": user["email"]})
    if not existing:
        users.insert_one(user)
        print(f"Email {user['email']} created.")
    else:
        print(f"Email {user['email']} already exists.")
        
