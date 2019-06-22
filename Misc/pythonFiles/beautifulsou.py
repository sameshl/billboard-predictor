# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Beautifulsoup class for scraping Artist Score.
In order to use the code import class Arist Score
'''

from bs4 import BeautifulSoup
import requests

class ArtistScore:
    '''
    This Class Provides Artist Handles for Youtube, Twitter, Instagram, Facebook.
    This Program uses beautifulsoup to parse through the XML document of NextBigSound Artist
    Metrics and scrape out their social media handles.
    Atributtes:
        PageNumber : The Page Number of XML document of an artist.
        Year : The year during which the popularity of the artist is to be extracted.
    '''
    def __init__(self, PageNumber, Year, fetch=True, timeout =25):
            self.PageNumber = PageNumber
            self.Year = Year
            self._timeout = timeout
            
    def FetchHandles(self):
        '''
        page stores the xml document.
        '''
        url = 'http://key.api3.nextbigsound.com/metrics/artist/%s' % (self.PageNumber)
        page = requests.get(url,timeout=self._timeout)
        
        if page.status_code == 404:
            message="Artist not found"
            raise Exception(message)
        page.raise_for_status()
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        '''
        url is the the URL of the NextBigSound XML document.
        '''
        
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
    pagenumber = 357
    year = 2007
    fetchhandles = ArtistScore(PageNumber = pagenumber, Year = year)  
    handle = fetchhandles.FetchHandles()
                