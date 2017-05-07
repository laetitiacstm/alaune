    # -*- coding:utf-8 -*-
     
import urllib, lxml.html
import methode_extraction


     
def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    articles= doc.xpath("//div[@class='main-article']//article/h2/a/text()")
    articles+= doc.xpath('//div[@class="title-wrapper"]//a/text()')
    articles+= doc.xpath('//div[@class="title-river"]//a/text()')
    
    liens = doc.xpath('//div[@class="main-article"]/article/h2/a/@href')
    liens+= doc.xpath('//div[@class="title-wrapper"]//a/@href')
    liens+= doc.xpath('//div[@class="title-river"]//a/@href')
    
    titres= zip(articles, liens)
    quotidien={'nom':'La Tribune', 'URL':targetURL}
    methode_extraction.extraction ('', quotidien, titres)
   


