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
menu_items = selections.find_all('dl')

# Loop over the menu items and parse the info
# Items to look for in the menu items:
#   Number, Hot, Item, Price
item = menu_items[0].find_all('dd')
number = ''
hot = False
item_name = ''
price = ''
for parts in item:
    if parts['class'] == ['number']:
        number = parts.text
    if parts['class'] == ['item']:
        item_name = parts.text
    if parts['class'] == ['price']:
        price = parts.text

print(
    f'Info gathered - Number: {number} - Hot: {hot} - Item: {item_name} - Price: {price}')


# Pass parsed info into a .csv file
