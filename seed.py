#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import *
import datetime


def run_test():

    client.drop_database(DATABASE_NAME)

    # add some departments
    dekanlik = add_dept("dekanlık")
    fakulte = add_dept("fakülte")
    set_parent_dept(fakulte,dekanlik)
    bolum = add_dept("bilgisayar bölümü")
    set_parent_dept(bolum,fakulte)

    # add some users
    ahmet = add_user("ahmet","tester","testerahmet@seyahdoo.com","1234","05062609999")
    mahmut = add_user("mahmut","tester","testermahmut@seyahdoo.com","1234","05062601111")
    recai = add_user("recai","deli","testerrecai@seyahdoo.com","4321","05062604798")
    halil = add_user("halil","cozucu","testerhalil@seyahdoo.com","1234","05062602222",fakulte,True,"teknisyen")
    yonetici = add_user("yonetici","bro","yonetici@seyahdoo.com","1234","05062602222",fakulte,True,"bolum_baskani")
    amir = add_user("amir","bro","amir@seyahdoo.com","1234","05062602222",fakulte,True,"amir")
    teknisyen = add_user("teknisyen","bro","teknisyen@seyahdoo.com","1234","05062602222",fakulte,True,"teknisyen")

    issue1= add_issue(fakulte,ahmet,"sikayet","Cam sıkıntısı","Cam kırık sanki :/")
    issue2= add_issue(fakulte,ahmet,"sikayet","Yer ıslak","d108 önü ıslak sanırım")
    issue3= add_issue(fakulte,mahmut,"itiraz","Notlar aşırı güzel","Dahada güzel olabilir")
    issue4= add_issue(fakulte,ahmet,"oneri","Notları düzeltelim","Kesinlikle güzel bi çözüm yolu bulabiliriz")

    assign_solver_to_issue(issue1, halil)

    update_issue(issue1, halil, "cozum_basladi")
    update_issue(issue1, halil, "cozuldu")
    update_issue(issue3, amir, "cozulemez")


if __name__ == "__main__":
    #"date": datetime.datetime.utcnow()
    run_test()
