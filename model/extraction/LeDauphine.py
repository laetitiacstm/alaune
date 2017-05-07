# -*- coding:utf-8 -*-
     
import urllib, lxml.html
import methode_extraction

     
def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    titres=doc.xpath("//a[@class='titre']/text()")
    liens=doc.xpath("//a[@class='titre']/@href")
   
    titres= zip(titres, liens)
    quotidien={'nom':'Le Dauphiné Libéré', 'URL':targetURL}
    methode_extraction.extraction (targetURL, quotidien,titres)
