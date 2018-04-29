
import database
import datetime

if __name__ == "__main__":

    post = {"author": "mikey",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    post_id = database.posts.insert_one(post).inserted_id

    print(post_id)
