#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

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

def add_issue(department,issuer,type,summary,text):
    issue = {
        "department_id":department,
        "issuer_id": issuer,
        "solver_id": None,
        "issue_type": type,
        "issue_status": "girildi",
        "entry_date": datetime.datetime.utcnow(),
        "finish_date": None,
        "issue_summary": summary,
        "detail_text":text,
        "attachments": [] ,
        "logs": [],
        "reports": [],
        "interruptions": []
        }
    issue_id = issues.insert_one(issue).inserted_id
    return issue_id

def get_issues(user_id):
    user = users.find_one({"_id": ObjectId(user_id)})
    role = user["role"]
    if (role=="mesele_girici"):
        print(role);
        issue_list=issues.find({"issuer_id":user_id})
        return issue_list
    elif(role=="amir" or role=="bolum_baskani"):
        department=user["worked_department"]
        issue_list=issues.find({"department_id":department})
        return issue_list
    elif(role=="teknisyen"):
        issue_list=issues.find({"solver_id": user_id})
        return issue_list
    elif(role=="admin"):
        return issues.find_all()
    return []


def set_parent_dept(child_department,parent_department):

    departments.find_one_and_update({"_id": parent_department},
                                    {"$set": {"child_department": child_department}})

    departments.find_one_and_update({"_id": child_department},
                                    {"$set": {"parent_department": parent_department}})

    return True

def update_issue(issue_id,user_id,status,message,attachment_url):

    #issue = issues.find_one("_id":issue_id)

    #TODO add message vs

    issues.find_one_and_update({"_id": child_department},
                                    {"$set": {"issue_status": status}})

    return

def assign_solver_to_issue(issue_id,solver_id):
    user = users.find_one({"_id": solver_id})
    user["issue_list"].append(issue_id)

    users.find_one_and_update({"_id": solver_id},
                                {"$set": {"issue_list": user["issue_list"]}})

    return
