from pymongo import MongoClient
import datetime

DATABASE_NAME = "issue-tracker"

client = MongoClient()

db = client[DATABASE_NAME]

users = db.users
issues = db.issues
interruptions = db.interruptions
issuestates = db.issuestates
issuetypes = db.issuetypes
attachments = db.attachments
departments = db.departments
issuelogs = db.issuelogs
issuereports = db.issuereports

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
        "role": role,
        "issue_list": []
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

def add_issue():
        issue={
            "issue_id"
            "department_id"
            "issuer_id"

        }
         =
         = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
         = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)#solver_id could be added
         = db.Column(db.Integer, db.ForeignKey('issuetypes.type_id'), nullable=True)
        state_id = db.Column(db.Integer, db.ForeignKey('issuestates.state_id'), nullable=True)
        entry_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
        finish_date = db.Column(db.DateTime, nullable=True)
        summary = db.Column(db.String(140), nullable=True)
        detail_text = db.Column(db.String(400), nullable=True)
        attachments = db.relationship("Attachment", backref=db.backref("issue_attachments"))
        logs= db.relationship("IssueLog",  backref=db.backref("logs"))
        reports=




def set_parent_dept(child_department,parent_department):

    departments.find_one_and_update({"_id": parent_department},
                                    {"$set": {"child_department": child_department}})

    departments.find_one_and_update({"_id": child_department},
                                    {"$set": {"parent_department": parent_department}})

    return True

def update_issue(issue_id,user_id,status,message,attachment_url):








    return
