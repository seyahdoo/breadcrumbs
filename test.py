#!/usr/bin/env python
# -*- coding: utf-8 -*-

from database import *
import datetime
import logic


def run_test():

    client.drop_database(DATABASE_NAME)

    # add some users
    ahmet = logic.add_user("ahmet","tester","testerahmet@seyahdoo.com","1234","05062609999")
    mahmut = logic.add_user("mahmut","tester","testermahmut@seyahdoo.com","1234","05062601111")
    recai = logic.add_user("recai","deli","testerrecai@seyahdoo.com","4321","05062604798")
    halil = logic.add_user("halil","tester","testerhalil@seyahdoo.com","1234","05062602222",None,True,"technitian")

    # add some departments
    dekanlik = logic.add_dept("dekanlık")
    fakulte = logic.add_dept("fakülte")
    logic.set_parent_dept(fakulte,dekanlik)
    bolum = logic.add_dept("bilgisayar bölümü")
    logic.set_parent_dept(bolum,fakulte)

    # add some issues entered by different user
    issue1 = {
        "department_id": bolum,
        "issuer_id": ahmet,
        "solver_id": None,
        "type": "oneri",
        "state": "girildi",
        "entry_date": datetime.datetime.utcnow(),
        "finish_date": None,
        "summary": "sorun sistemi lütfen",
        "detail_text": "sorunlarımızı girebileceğimiz bir sistem yapın lütfen",
        "attachments": [],
        "logs": [],
        "reports": [],
        "interruptions": []
    }
    issue1_id = issues.insert_one(issue1).inserted_id

    # assign issues to certain technitians
    issues.find_one_and_update({"_id": issue1_id},
                                {"$set": {
                                "solver_id": halil,
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
