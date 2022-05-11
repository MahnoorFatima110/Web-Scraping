import urllib.request as rq
from bs4 import BeautifulSoup as soup
import preprocessor as p

myURL = 'https://en.wikipedia.org/wiki/Pakistan'
req=rq.Request(myURL,headers={'User-Agent':'Mozilla/5.0'})
page_html= rq.urlopen(req).read()
page_soup=soup(page_html,"html.parser")
docFile= open('2k19.txt','w+')
for contain in page_soup.find_all("div", {"class":"mw-parser-output"}):
    docFile.writelines(p.clean(str(contain.get_text().encode('utf-8'))))
docFile.close()
