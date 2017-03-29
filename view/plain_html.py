# -*- coding:utf-8 -*-

def simple_form():
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
	page_content += '<option value="ouestfrance">Ouest France</option>'
	page_content += '<option value="sudouest"> Le Sud Ouest </option>'
	page_content += '<option value="leparisien">Le Parisien</option>'
	page_content += '<option value="20min">20 minutes</option>'

	page_content += '</select>'

	page_content += '<input type="submit" value="Envoyer"></input>'
	page_content += '</form>'
	return page_content

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
