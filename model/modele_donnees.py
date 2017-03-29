#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mysql.connector
import json

def insert_quotidien(data_quotidien):
    '''
    la fonction effectue une insertion d'un nouveau quotidien
    dans la base de donnees
    la variable quotidien contient un dictionnaire décrivant le quotidien
    '''
    config = json.loads(open('config', 'r').read())
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    add_quotidien = ("INSERT INTO quotidiens (nom, nom_court, URL) VALUES (%(nom)s, %(nom_court)s, %(URL)s)")
    cursor.execute(add_quotidien, data_quotidien)
    cnx.commit()

def select_quotidien(nom_court_quotidien):
    '''
    la fonction effectue une requete sur la base pour trouver
    les information sur un quotidien a partir de son nom
    -- utile lorsqu'une autre fonction doit obtenir la cle primaire d'un quotidien
    '''
    config = json.loads(open('config', 'r').read())
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    get_quotidien = ("SELECT id, URL FROM quotidiens WHERE nom_court LIKE (%(nom_court)s)")
    data_quotidien = {'nom_court': nom_court_quotidien}
    cursor.execute(get_quotidien, data_quotidien)
    if cursor.rowcount == 0:
        return None
    else:
        id, URL = row = cursor.fetchone()
        return id, URL

def insert_une(une):
    '''
    la fonction effectue une insertion d'un nouveau quotidien
    dans la base de donnees
    la variable une contient un dictionnaire décrivant la une
    la fonction devra auparavant interroger la base pour connaitre
    le id du quotidien apparaissant en cle etrangere dans la table unes
    '''
    config = json.loads(open('config', 'r').read())
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    id, URL = select_quotidien(une['nom_court_quotidien'])
    add_une = ("INSERT INTO unes (titre, URL, quotidien_id) VALUES (%(titre)s, %(URL)s, %(quotidien_id)s)")
    une['quotidien_id'] = id
    print '**********', une
    cursor.execute(add_une, une)
    cnx.commit()

def select_unes(nom_quotidien):
    '''
    la fonction effectue une requete sur la base pour trouver
    les unes d'un quotidien
    on peut imaginer des variantes permettant de cibler une date, un mot, etc.
    '''
    config = json.loads(open('config', 'r').read())
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    quotidien_id, quotidien_URL = select_quotidien(nom_quotidien)
    print 'Quotidien id ', quotidien_id
    get_unes = ("SELECT titre, URL, date FROM unes WHERE quotidien_id = (%(quotidien_id)s)")
    data_unes = {'quotidien_id': quotidien_id}
    cursor.execute(get_unes, data_unes)
    if cursor.rowcount == 0:
        return None
    else:
        unes = []
        for row in cursor:
            unes.append(row)
        print unes
        return unes, quotidien_URL

if __name__ == '__main__':
    #data_quotidien = {'nom': 'Le Figaro', 'nom_court': 'lefigaro', 'URL': 'www.lefigaro.fr'}
    #print select_unes('lefigaro')
    une = {'titre': 'Un titre', 'nom_court_quotidien': 'lemonde', 'URL': '/societe/article/2017/03/28/guyane-nous-sommes-en-france-mais-pas-vraiment-consideres-comme-francais_5102103_3224.html'}
    insert_une(une)

