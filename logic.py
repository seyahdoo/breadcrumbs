from database import *

def add_user(
        first_name,
        last_name,
        email,
        password,
        phone_number,
        worked_department = None,
        active = True,
        role = "mesele_girici"):

    user = {
        "phone_number": phone_number,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "worked_department": worked_department,
        "active": active,
        "role": role
    }
    user_id = users.insert_one(user).inserted_id

    return user_id
