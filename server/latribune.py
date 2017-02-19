
import urllib, lxml.html
 
 
def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//div[@class="title-wrapper"]/h2/a/@href') 
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//div[@class="title-wrapper"]/h2/a/text()')
 
	return zip(article_titles, articles_href)
