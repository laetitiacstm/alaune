# -*- coding:utf-8-*-

from model import modele_donnees
from datetime import datetime


def extraction ( url_journal, quotidien, titres):
        date= datetime.now().strftime('%Y-%m-%d ')
        for t in titres:
                titre = t[0]
                URL = url_journal + t[1]
                une = {}
                une['url'] = str(URL)
                une['titre'] = titre.encode('utf8')
                une['date']=date
                modele_donnees.insert_une(une,quotidien)
        return True
