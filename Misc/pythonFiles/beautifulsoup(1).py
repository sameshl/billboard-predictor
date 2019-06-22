# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Beautifulsoup class for scraping Artist Score.
In order to use the code import class Arist Score
'''

from bs4 import BeautifulSoup, CData
import requests
import urllib3

class ArtistScore:
    '''
    This Class Provides Artist Handles for Youtube, Twitter, Instagram, Facebook.
    This Program uses beautifulsoup to parse through the XML document of NextBigSound Artist
    Metrics and scrape out their social media handles.
    Atributtes:
        PageNumber : The Page Number of XML document of an artist.
        Year : The year during which the popularity of the artist is to be extracted.
    '''
    def __init__(self, Artist, fetch=True, timeout =25):            
            self.id = ''
            self._timeout = timeout
            self.Artist = Artist
            
    def FetchId(self):
        '''
        Fetches the id of the Artist
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url = 'https://key.api3.nextbigsound.com/artists/search.xml?q=%s' % (self.Artist)
        page = requests.get(url, verify = False)
        
        if page.status_code == 404:
            message="ID not found"
            raise Exception(message)
        page.raise_for_status()
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        l = soup.find_all('name')
        print (l)
        
        i=0
        Links = list()
        l = len(soup.find_all('name'))
        Links = list()
        for cd in soup.findAll(text=True):
            if isinstance(cd, CData):
                Links.append(cd)
                s = Links[i]
                if s == self.Artist:
                    count = i
                    i=i+1
                    self.id = soup.find('artistid')[count]
                    break
                else:
                    continue
        return self.id
        
        
        
    def FetchHandles(self):
        '''
#        Fetches the social media accounts of Artists
#        page stores the xml document.
#        url is the the URL of the NextBigSound XML document.
        '''
        url = 'http://key.api3.nextbigsound.com/metrics/artist/%s' % (self.id)
        page = requests.get(url,timeout=self._timeout)
        
        if page.status_code == 404:
            message="Artist not found"
            raise Exception(message)
        page.raise_for_status()
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        Links = list()
        l = len(soup.find_all('url'))
        for i in range(l-1):
            # Link Stores the urls of the social media home pages of the Artists
            Links.append(soup.find_all('url')[i].get_text())
            s = Links[i]
            # The statement check to find the url for twitter
            if "twitter" in s:
                s = s.replace('http://twitter.com/', '')
                break
            else:
                continue

        return s
        
'''
Checks if the given program is working or not.
'''
if __name__ == '__main__':
    Id = 357
    year = 2007
    fetchid = ArtistScore(Artist = 'The Weeknd')  
    handle = fetchid.FetchId()
                