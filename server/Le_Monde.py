#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
app = Flask (__name__)

import lemonde

@app.route('/')
def index():
    page_content = ''
    page_content += '<h2> Choisissez votre journal : </h2>'
    page_content += '<from action = "/quel_journal" method="post" >'
    page_content += '<select name = "journal" >'
    page_content += '<option value = "liberation">Libération</option>'
    page_content += '<option value = "lemonde">Le Monde</option>'
    page_content += '<option value = "figaro">Le Figaro</option>'
    page_content += '<option value = "courrier">Courrier International</option>'
    page_content += '</select>'
    page_content += '<input type="submit" value="Envoyer"></imput>'
    page_content += '</form>'
    return page_content


@app.route('/quel_journal', methods = ['POST'])
def quel_journal() :
    journal = request.form['journal']
    if journal == 'lemonde':
        targetURL = 'http://www.lemonde.fr'
        titres= lemonde.unes(targetURL)
        return htmlize(titres, targetURL)
    else:
        return journal

def htmlize(titles_and_href, targetURL):
    html = ''
    for item in titles_and_href:
        html += '<h2>'
        html += '<a href="' + targetURL + item[1] + '">' + item[0].strip() + '</a></h2>\n'
    return html

if __name__ == '__main__':
    app.run(debug=True)
