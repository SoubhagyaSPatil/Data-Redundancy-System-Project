import firebase_admin
from firebase_admin import credentials, db

# Load key
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://data-redundancy-system-task-default-rtdb.asia-southeast1.firebasedatabase.app"
})

# Reference to users
ref = db.reference("users")

# Add new data
ref.push({

    "name": "Alice",
    "email": "alice@gmail.com"
})

print(" Data added to Firebase")