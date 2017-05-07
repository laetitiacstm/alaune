# -*- coding:utf-8 -*-

import mysql.connector
import json


config = json.loads(open('config.json', 'r').read())
cnx = mysql.connector.connect(** config)
cursor = cnx.cursor(buffered=True)


def insert_quotidien(quotidien):
    cursor.execute ("SELECT nom FROM quotidiens WHERE nom LIKE (%(nom)s)", quotidien)
    if (cursor.rowcount==0):
        add_quotidien = ("INSERT INTO quotidiens (id, nom, URL) VALUES (NULL,%(nom)s, %(URL)s)")
        cursor.execute(add_quotidien, quotidien)
        cnx.commit()
    



def insert_une(une,quotidien):
    cursor.execute ("SELECT titre FROM unes WHERE titre LIKE (%(titre)s) ", une)
    if (cursor.rowcount==0):
        print 'Nouvelle une'
        get_quotidien=("SELECT id FROM quotidiens WHERE nom LIKE (%(nom)s)")
        cursor.execute(get_quotidien,quotidien)
        id_quotidien=cursor.fetchone()[0]
        une['quotidien_id']=id_quotidien
        add_une=("INSERT INTO unes (id, titre, url, date, quotidien_id) VALUES (NULL, %(titre)s, %(url)s, %(date)s, %(quotidien_id)s)")
        cursor.execute(add_une, une)
        cnx.commit()

    


def select_unes_today(quotidien):
    get_quotidien = ("SELECT id FROM quotidiens WHERE nom LIKE  %(nom)s")
    quot_data= {'nom':quotidien}
    cursor.execute(get_quotidien, quot_data)
    id_quotidien=cursor.fetchone()[0]
    une={'quotidien_id':id_quotidien}
    nom_une = ("SELECT titre,url  FROM unes WHERE quotidien_id LIKE %(quotidien_id)s AND date=CURDATE()")
    cursor.execute(nom_une,une)
    result=cursor.fetchall()
    return result

def select_unes_nom(nom):
    cursor.execute("SELECT titre, url FROM unes WHERE titre LIKE '%"+nom+"%' ORDER BY date DESC  ")
    result=cursor.fetchall()
    return result

def select_unes_nom_date_journal(nom):
    cursor.execute("SELECT titre, unes.url, DATE_FORMAT(date, '%d-%m-%Y') as datefr, quotidiens.nom FROM unes INNER JOIN quotidiens ON quotidiens.id=quotidien_id WHERE titre LIKE '%"+nom+"%'   ORDER BY date DESC, quotidiens.id  ")
    result=cursor.fetchall()
    return result


def count_unes (nom):
    cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%"+nom+"%' ")
    count = 0
    for row in cursor :
        count+=1
    return count
    
def count_unes_journal (nom,journal):
    cursor.execute("SELECT titre FROM unes INNER JOIN quotidiens ON quotidiens.id=quotidien_id WHERE titre LIKE '%"+nom+"%'  AND quotidiens.nom = '"+journal+"';")
    count = 0
    for row in cursor :
        count+=1
    return count


def count_unes_avant(nom):
    cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%"+nom+"%' AND date<= '2017-04-23'")
    count = 0
    for row in cursor :
        count+=1
    return count

def count_unes_apres(nom):
    cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%"+nom+"%'  AND date>'2017-04-23'")
    count = 0
    for row in cursor :
        count+=1
    return count


    




    

if __name__== '__main__':
    '''quotidien = { 'nom': 'La Presse', 'URL' : 'www.lapresse.ca' }
    insert_quotidien(quotidien)
    une={}
    une['titre']="Devant le Congrès, Trump fait l'éloge d'une «nouvelle fierté nationale»"
    une['url']='international/etats-unis/201702/28/01-5073982-devant-le-congres-trump-fait-leloge-dune-nouvelle-fierte-nationale.php'
    une['date'] = '2017-03-07'
    une['quotidien_id']='1'

    insert_une(une, quotidien)'''
    #select_unes_nom('20 minutes')
    count_unes_journal('Fillon','Le Parisien')
    
    
