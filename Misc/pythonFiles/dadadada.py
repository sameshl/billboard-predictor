from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import xml.etree.ElementTree as ET


Artist='The Weeknd'
url='https://key.api3.nextbigsound.com/artists/search.xml?q=%s' %(Artist)

page=requests.get(url,verify=False).text

soup=BeautifulSoup(page,'lxml')
print(soup.prettify())



match=soup.find_all('artist')
#print(match)

#print(soup)
#artist=soup.find_all('artist')
#print(artist)

#e = ET.parse(soup.is_xml).getroot()

#tree = ET.parse(soup)d