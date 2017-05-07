#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
from datetime import datetime
from model import modele_extraction, modele_donnees
from view import plain_html
import jinja2

app = Flask('A la une')
app.jinja_loader=jinja2.FileSystemLoader('./view/templates')

@app.route('/')
def index():
        modele_extraction.extraction_all()
        count1=modele_donnees.count_unes('Macron')
        count2=modele_donnees.count_unes('Mélenchon')
        count3=modele_donnees.count_unes('Le Pen')
        count4=modele_donnees.count_unes('Hamon')
        count5=modele_donnees.count_unes('Fillon')
        return render_template('accueil.html' ,quantite1=count1, quantite2=count2, quantite3=count3,quantite4=count4, quantite5=count5)  

@app.route('/journaux')
def choix():
        return render_template('choix.html')

@app.route('/journal', methods = ['POST'])
def quel_journal():
        journal = request.form['journal']
        result = modele_donnees.select_unes_today(journal)
        return render_template('queljournal.html', quantite=journal) +plain_html.htmlize(result)


@app.route('/click/<nom>')
def unes_nom(nom):
        nom=plain_html.arranger_id(nom)
        result = modele_donnees.select_unes_nom_date_journal(nom)
        count1=modele_donnees.count_unes_journal(nom,'20 minutes')
        count2=modele_donnees.count_unes_journal(nom,'Courrier International')
        count3=modele_donnees.count_unes_journal(nom,'La Tribune')
        count4=modele_donnees.count_unes_journal(nom,'Le Dauphiné Libéré')
        count5=modele_donnees.count_unes_journal(nom,'Le Figaro')
        count6=modele_donnees.count_unes_journal(nom,'Le Journal du Net')
        count7=modele_donnees.count_unes_journal(nom,'Le Parisien')
        count8=modele_donnees.count_unes_journal(nom,'Le Point')
        count9=modele_donnees.count_unes_journal(nom,'Les Echos')
        count10=modele_donnees.count_unes_journal(nom,'Sud Ouest')
        return render_template('click.html',mot=nom.decode('utf-8'), quantite1=count1, quantite2=count2, quantite3=count3,quantite4=count4, quantite5=count5, quantite6=count6,quantite7=count7,quantite8=count8,quantite9=count9,quantite10=count10)+ plain_html.htmlize2(result)


        
@app.route('/avant_1er_tour')
def unes_avant():
        count1=modele_donnees.count_unes_avant('Macron')
        count2=modele_donnees.count_unes_avant('Mélenchon')
        count3=modele_donnees.count_unes_avant('Le Pen')
        count4=modele_donnees.count_unes_avant('Hamon')
        count5=modele_donnees.count_unes_avant('Fillon')
        return render_template('avant.html' ,quantite1=count1, quantite2=count2, quantite3=count3,quantite4=count4, quantite5=count5) 

@app.route('/apres_1er_tour')
def unes_apres():
        count1=modele_donnees.count_unes_avant('Macron')
        count2=modele_donnees.count_unes_avant('Le Pen')
        return render_template('apres.html' ,quantite1=count1, quantite2=count2)


if __name__ == '__main__':
	app.run(debug=True)



