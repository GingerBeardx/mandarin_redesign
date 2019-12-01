"""
This is a simple script to get the menu data from the Mandarin Garden Lunch
Specials page, gather the necessary info, serialize it, and then pass it into
a csv file.

Author: Eric Greenhalgh
Created: November 29, 2019
"""

# python3

# native imports
import urllib.request as urlReq
import csv

# downloaded imports
from bs4 import BeautifulSoup as bs

# Get the Mandarin Garden WebSite Lunch Specials page
with urlReq.urlopen('http://mandaringarden.biz/lunch.html') as f:
    specials_page = f.read()

# Convert the Specials page into soup to prepare for parsing
soup = bs(specials_page, 'html.parser')
selections = soup.find(id='lunchlist')
menu_items = selections.find_all('dl')
menu_items_list = []

# Loop over the menu items and parse the info
# Items to look for in the menu items:
#   Number, Hot, Item, Price
for item_list in menu_items:
    item = item_list.find_all('dd')
    number = ''
    hot = False
    item_name = ''
    price = ''
    item = item_list.find_all('dd')
    for parts in item:
        if parts['class'] == ['number']:
            number = parts.text.strip()
            if parts.img is not None:
                hot = True
        if parts['class'] == ['item']:
            item_name = parts.text.lower()
        if parts['class'] == ['price']:
            price = parts.text
    item_dict = {
        'name': f"{number}", 'hot': f"{hot}",
        'item': f"{item_name}", 'price': f"{price}"
    }
    menu_items_list.append(item_dict)

# Pass parsed info into a .csv file
with open('lunch_specials.csv', 'w', newline='') as f:
    field_names = ['name', 'hot', 'item', 'price']
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    for menu_item in menu_items_list:
        writer.writerow(menu_item)
