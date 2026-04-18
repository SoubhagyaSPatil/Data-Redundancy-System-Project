import firebase_admin
from firebase_admin import credentials, db

# Connect to Firebase
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-redundancy-system-task-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference("users")
ref.push({

    "name": "Alice",
    "email": "alice@gmail.com"
})

print(" Data added to Firebase")

# -------- Functions --------

def validate_data(data):
    if data["name"] == "":
        
        return "Invalid"
    if "@" not in data["email"]:
        return "Invalid"
    return "Valid"

def check_duplicate(data):
    users = ref.get()
    if users:
        for key in users:
            if users[key]["email"] == data["email"]:
                return True
    return False

def classify_data(data):
    if validate_data(data) == "Invalid":
        return "Invalid"
    elif check_duplicate(data):
        return "Duplicate"
    else:
        return "Valid"

# -------- Main Program --------

data = {
    "name": input("Enter Name: "),
    "email": input("Enter Email: ")
}

result = classify_data(data)

if result == "Valid":
    ref.push(data)
    print(" Data Stored in Firebase")
elif result == "Duplicate":
    print(" Duplicate Data - Not Stored")
else:
    print("Invalid Data")


