import csv
import json

# Make a dictionary with attributes of menu header and file name
menu = [
    {
        'header': 'Appetizers',
        'filename': 'apetizers.csv'
    },
    {
        'header': 'Beef',
        'filename': 'beef.csv'
    },
    {
        'header': 'Chow Mein',
        'filename': 'chow-mein.csv'
    },
    {
        'header': 'Egg Foo Young',
        'filename': 'egg-foo-young.csv'
    },
    {
        'header': 'Fried Rice',
        'filename': 'fried_rice.csv'
    },
    {
        'header': 'Lo Mein',
        'filename': 'lo-mein.csv'
    },
    {
        'header': 'Pork',
        'filename': 'pork.csv'
    },
    {
        'header': 'Poultry',
        'filename': 'poultry.csv'
    },
    {
        'header': 'Seafood',
        'filename': 'seafood.csv'
    },
    {
        'header': 'Soups',
        'filename': 'soups.csv'
    },
    {
        'header': 'Specials',
        'filename': 'specials.csv'
    },
    {
        'header': 'Specials 2',
        'filename': 'specials_2.csv'
    },
    {
        'header': 'Vegetables',
        'filename': 'vegetables.csv'
    }
]
# Loop over the menu variable to create the full menu


def generate_menu():
    full_menu = []
    for menu_item in menu:
        menu_dict = {}
        menu_dict['header'] = menu_item['header']
        with open('./scrape/' + menu_item['filename']) as f:
            menu_items = list(csv.DictReader(f))
        menu_dict['item_list'] = menu_items
        full_menu.append(menu_dict)
    return full_menu
