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

posts = db.posts


if __name__ == "__main__":

    post = {"author": "mikey",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    post_id = posts.insert_one(post).inserted_id

    print(post_id)






