#!/usr/bin/env python
# -*- coding: utf-8 -*-

from database import *
import datetime

def run_test():

    client.drop_database(DATABASE_NAME)


    # add some users
    user1 = {
        "phone_number": "05062609999",
        "email": "testerahmet@seyahdoo.com",
        "password": "1234",
        "first_name": "ahmet",
        "last_name": "tester",
        "worked_department": None,
        "active": True,
        "role": "mesele_girici"
    }
    user1_id = users.insert_one(user1).inserted_id

    user2 = {
        "phone_number": "05062601111",
        "email": "testeryilmaz@seyahdoo.com",
        "password": "1234",
        "first_name": "yilmaz",
        "last_name": "tester",
        "worked_department": None,
        "active": True,
        "role": "mesele_girici"
    }
    user2_id = users.insert_one(user2).inserted_id

    tech1 = {
        "phone_number": "05062602222",
        "email": "testermahmut@seyahdoo.com",
        "password": "1234",
        "first_name": "mahmut",
        "last_name": "tester",
        "worked_department": None,
        "active": True,
        "role": "technitian"
    }
    tech1_id = users.insert_one(tech1).inserted_id

    # add some departments
    dept1 = {
        "parent_department": None,
        "child_department": None,
        "name": "dekanlik",
        "issuelist": []
    }
    dept1_id = departments.insert_one(dept1).inserted_id

    dept2 = {
        "parent_department": None,
        "child_department": None,
        "name": "fakulte",
        "issuelist": []
    }
    dept2_id = departments.insert_one(dept2).inserted_id

    departments.find_one_and_update({"_id": dept1_id},
                                    {"$set": {"child_department": dept2_id}})

    departments.find_one_and_update({"_id": dept2_id},
                                    {"$set": {"parent_department": dept1_id}})

    # add some issues entered by different user
    issue1 = {
        "department_id": dept2_id,
        "issuer_id": user1_id,
        "solver_id": None,
        "type": "oneri",
        "state": "girildi",
        "entry_date": datetime.datetime.utcnow(),
        "finish_date": None,
        "summary": "sorun sistemi lütfen",
        "detail_text": "sorunlarımızı girebileceğimiz bir sistem yapın lütfen",
        "attachments": [],
        "logs": [],
        "reports": []
        "interruptions": []
    }
    issue1_id = issues.insert_one(issue1).inserted_id

    # assign issues to certain technitians
    issues.find_one_and_update({"_id": issue1_id},
                                {"$set": {
                                "solver_id": tech1_id,
                                "state": "cozum_basladi"
                                }})


    # make them solve it
    issues.find_one_and_update({"_id": issue1_id},
                                {"$set": {
                                "state": "cozuldu"
                                }})



    # fin

if __name__ == "__main__":

    run_test()
