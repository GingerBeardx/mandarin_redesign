"""
This is a simple script to get the menu data from the Mandarin Garden Website.

Author: Eric Greenhalgh
Created: November 29, 2019
"""

# python3

# native imports
import urllib.request as urlReq

# downloaded imports
from bs4 import BeautifulSoup as bs

# Get the Mandarin Garden WebSite Lunch Specials page
with urlReq.urlopen('http://mandaringarden.biz/lunch.html') as f:
    specials_page = f.read()

# Convert the Specials page into soup to prepare for parsing
soup = bs(specials_page, 'html.parser')
selections = soup.find(id='lunchlist')
