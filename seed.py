#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import *
import datetime


def run_test():

    client.drop_database(DATABASE_NAME)

    # add some users
    ahmet = add_user("ahmet","tester","testerahmet@seyahdoo.com","1234","05062609999")
    mahmut = add_user("mahmut","tester","testermahmut@seyahdoo.com","1234","05062601111")
    recai = add_user("recai","deli","testerrecai@seyahdoo.com","4321","05062604798")
    halil = add_user("halil","cozucu","testerhalil@seyahdoo.com","1234","05062602222",None,True,"technitian")

    # add some departments
    dekanlik = add_dept("dekanlık")
    fakulte = add_dept("fakülte")
    set_parent_dept(fakulte,dekanlik)
    bolum = add_dept("bilgisayar bölümü")
    set_parent_dept(bolum,fakulte)


    issue1= add_issue(fakulte,ahmet,"sikayet","hello","sorun konu")
    issue2= add_issue(fakulte,ahmet,"sikayet","heyy","sorun konu")
    issue3= add_issue(fakulte,mahmut,"itiraz","hiii","sorun konu sudur")
    issue4= add_issue(fakulte,ahmet,"oneri","hello","sorun konusu bu")






    # assign issues to certain technitians
    issues.find_one_and_update({"_id": issue1},
                                {"$set": {
                                "solver_id": halil,
                                "state": "cozum_basladi"
                                }})


    # make them solve it
    issues.find_one_and_update({"_id": issue2},
                                {"$set": {
                                "state": "cozuldu"
                                }})

    # fin


if __name__ == "__main__":
    #"date": datetime.datetime.utcnow()
    run_test()
