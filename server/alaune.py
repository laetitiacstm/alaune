#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Commentaire de Laura
from flask import Flask, request

import CourrierInternational, LePoint, JournalduNet, lesechos, LeDauphine, LaTribune1, sudouest, LeFigaro, LeParisien, _20minutes

app = Flask('A la une')

@app.route('/')
def index():
	page_content = ''
	page_content += '<h2>Choisissez votre journal:</h2>'
	page_content += '<form action="/quel_journal" method="post">'

	page_content += '<select name="journal">'
	page_content += '<option value="liberation">Libération</option>'
	page_content += '<option value="lemonde">LeMonde</option>'
	page_content += '<option value="figaro">Le Figaro</option>'
	page_content += '<option value="lejournaldunet">Le Journal du Net</option>'
	page_content += '<option value="lepoint">Le Point</option>'
	page_content += '<option value="courrier">Courrier International</option>'
	page_content += '<option value="lesechos">Les Echos</option>'
	page_content += '<option value="latribune">La Tribune</option>'
	page_content += '<option value="ledauphine"> Le Dauphiné Libéré </option>'
	page_content += '<option value="sudouest"> Le Sud Ouest </option>'
	page_content += '<option value="leparisien">Le Parisien</option>'
	page_content += '<option value="20min">20 minutes</option>'
	page_content += '</select>'

	page_content += '<input type="submit" value="Envoyer"></input>'
	page_content += '</form>'
	return page_content

@app.route('/quel_journal', methods = ['POST'])
def quel_journal():
	journal = request.form['journal']
	if journal == 'courrier':
		targetURL = 'http://www.courrierinternational.com'
		titres = CourrierInternational.unes(targetURL)
		return htmlize(titres, targetURL)
	elif journal == 'lepoint':
		targetURL = 'http://www.lepoint.fr'
		titres = LePoint.unes(targetURL)
		return htmlize(titres, targetURL)
	elif journal == 'lejournaldunet':
		targetURL = 'http://www.lejournaldunet.fr'
		titres = JournalduNet.unes(targetURL)
		return htmlize2(titres)
	elif journal == 'lesechos':
		targetURL = 'http://www.lesechos.fr/'
		titres = lesechos.unes(targetURL)
		return htmlize2(titres)
	elif journal == 'latribune':
		targetURL = 'http://www.latribune.fr/'
		titres = LaTribune1.unes(targetURL)
		return htmlize2(titres)
	elif journal == 'ledauphine' :
		targetURL= 'http://ledauphine.com'
		titres=LeDauphine.unes(targetURL)
		return htmlize(titres,targetURL)
	elif journal == 'sudouest' :
		targetURL= 'http://www.sudouest.fr/'
		titres=sudouest.unes(targetURL)
		return htmlize(titres,targetURL)
	elif journal == 'figaro' :
		targetURL= 'http://www.lefigaro.fr/'
		titres=LeFigaro.unes(targetURL)
		return htmlize2(titres)
	elif journal=='leparisien':
		targetURL='http://www.leparisien.fr'
		titres=LeParisien.unes(targetURL)
		return htmlize2(titres)
	elif journal=='20min':
		targetURL='http://www.20minutes.fr'
		titres=_20minutes.unes(targetURL)
		return htmlize(titres,targetURL) 
        
	else:
		return journal

def htmlize(titles_and_href, targetURL):
	html = ''
	for item in titles_and_href:
		html += '<h2>'
		html += '<a href="' + targetURL + item[1] + '">' + item[0].strip() + '</a></h2>\n'
	return html

#### htmlize2 à la même fonction que htmlize mais sans répétition de targetURL
# du coup ça sert à rien de garder le paramètre targetURL, je le vire /Laura
def htmlize2(titles_and_href):
	html = ''
	for item in titles_and_href:
		html += '<h2>'
		html += '<a href="' + item[1] + '">' + item[0].strip() + '</a></h2>\n'
	return html
####

if __name__ == '__main__':
	app.run(debug=True)

