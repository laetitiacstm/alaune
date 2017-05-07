# -*- coding:utf-8 -*-
 
import urllib, lxml.html
import methode_extraction

 
 
def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//h2[@class="app_title"]/a/@href')
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//h2[@class="app_title"]/a/text()')
	
	titres= zip(article_titles, articles_href)
	quotidien={'nom':'Le Journal du Net', 'URL':targetURL}
	methode_extraction.extraction ('', quotidien,titres)
	
