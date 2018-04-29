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

def add_dept(name):

    dept = {
        "parent_department": None,
        "child_department": None,
        "name": name,
        "issuelist": []
    }
    dept_id = departments.insert_one(dept).inserted_id

    return dept_id

def set_parent_dept(child_department,parent_department):

    departments.find_one_and_update({"_id": parent_department},
                                    {"$set": {"child_department": child_department}})

    departments.find_one_and_update({"_id": child_department},
                                    {"$set": {"parent_department": parent_department}})

    return True
