#!/usr/bin/env python
# -*- coding:utf-8 -*-
import mysql.connector

## config est dans le .py pour les test
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'alaune',
}
##
link = mysql.connector.connect(**config)
cursor = cnx.cursor()


### le code n'est pas fini (je n'est pas vérifié le fonctionnement)
def insert_quotidien(** quotidien):
	add_quotidien = ("INSERT INTO quotidiens(nom, URL) VALUES (%(nom)s, %s)")
	data_quotidien = quotidien
	get_quotidien = ("SELECT id, URL FROM quotidiens WHERE nom LIKE (%(nom)s)")
	if (cursor.execute(get_quotidien, data_quotidien) == NULL):
		cursor.execute(add_quotidien, data_quotidien)
	
	

def insert_une(** une):
	add_une = ("INSERT INTO une (titre, URL, date, quotidien_id) VALUES (%(titre)s, %(URL)s, %(date)s)")
	quotidien_id = ("SELECT id, URL FROM quotidiens WHERE nom LIKE (%(nom)s)")
	data_une = une + quotidien_id
	cursor.execute (add_une,data_une)
    # to do
    # la variable une contient un dictionnaire décrivant la une
    # la fonction devra auparavant interroger la base pour connaitre
    # le id du quotidien apparaissant en cle etrangere dans la table unes
    
#def select_une(quotidien):
    # to do
    # la fonction devra auparavant interroger la base pour connaitre
    # le id du quotidien apparaissant en cle etrangere dans la table unes

if __name__ == '__main__':
    quotidien = {'nom': 'La Presse', 
    			 'url': 'www.lapressse.ca'
    			}
    insert_quotidien(quotidien)

    une = {}
    une['titre'] = "Devant le Congrès, Trump fait l'éloge d'une «nouvelle fierté nationale»"
    une['URL'] = 'international/etats-unis/201702/28/01-5073982-devant-le-congres-trump-fait-leloge-dune-nouvelle-fierte-nationale.php'
    une['date'] = '01/03/2017'
    insert_une(une)
    
    #select_une('La Presse')