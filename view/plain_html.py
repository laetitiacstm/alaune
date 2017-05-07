# -*- coding:utf-8 -*-




def htmlize(titles_and_href):
        html = ''
        html += '<ul>'
        for item in titles_and_href:
                html += '<li><a href="' + item[1] + '">' + item[0].strip() + '</a></li>'
        html+='</ul>'
        return html

def htmlize2(titles_and_href):
        html = ''
        html += '<ul>'
        for item in titles_and_href:
                html += '<li><a href="' + item[1] + '">' + item[0].strip() + '</a> , ' +item[2] +' , '+ item[3] +'</li>'
        html+='</ul>'
        return html

def arranger_id(nom):
        if nom=='dimple-all-fillon---':
                nom='Fillon'
        if nom =='dimple-all-macron---':
                nom='Macron'
        if nom=='dimple-all-m-lenchon---':
                nom='Mélenchon'
        if nom== 'dimple-all-le-pen---':
                nom='Le Pen'
        if nom== 'dimple-all-hamon---':
                nom='Hamon'
        return nom

