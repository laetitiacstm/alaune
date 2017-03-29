# -*- coding:utf-8 -*-

from flask import Flask, request

from view import plain_html
from model import modele_donnees

app = Flask(__name__)

@app.route('/')
def index():
	return plain_html.simple_form()

@app.route('/quel_journal', methods = ['POST'])
def quel_journal():
	journal = request.form['journal']
	unes, URL = modele_donnees.select_unes(journal)
	return plain_html.htmlize(unes, URL)

if __name__ == '__main__':
	app.run(debug=True)

