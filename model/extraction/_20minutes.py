#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib, lxml.html
import methode_extraction


def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
	doc = lxml.html.document_fromstring(data)
	articles_href =  doc.xpath('//article//h2/a/@href')
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//article//h2//text()')
	titres=zip(article_titles, articles_href)
	quotidien={'nom':'20 minutes', 'URL':targetURL}
	methode_extraction.extraction (targetURL, quotidien,titres)
 
	
	

	

