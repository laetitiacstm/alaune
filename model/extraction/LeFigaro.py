# -*- coding:utf-8 -*-
 
import urllib, lxml.html
import methode_extraction

 
def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//h1[@class="fig-profil-headline"]/a/@href') + doc.xpath('//section[contains(@class, "fig-profil ")]/div/h2/a/@href')
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//h1[@class="fig-profil-headline"]/a/text()') + doc.xpath('//section[contains(@class, "fig-profil ")]/div/h2/a/text()')
	
	titres= zip(article_titles, articles_href)
	quotidien={'nom':'Le Figaro', 'URL':targetURL}
	methode_extraction.extraction ('', quotidien,titres)
	
