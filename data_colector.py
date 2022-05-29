import requests as req
from bs4 import BeautifulSoup as BS
import csv
import sys
import os

MAIN_URL = 'https://volby.cz/pls/ps2017nss/'        # not actual link
FIELS_NAMES = 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103'

def argument_checker() -> bool:
    if len(sys.argv) != 3:
        return False
    else:
        return True


def web_searcher(path):
    r = req.get(path).text
    bsoup = BS(r, 'html.parser')
    return bsoup


def find_links(soup):
    main_val = soup.find_all('table', {'class': 'table'})
    additional_links = []
    for table in main_val:
        links = table.find_all('a', href=True)
        for link in links:
            if link.text == 'X':
                continue
            else:
                additional_links.append(link['href'])
    return additional_links


def getting_number():
    soup = web_searcher(sys.argv[1])
    numbers = soup.find_all('td', {'class': 'cislo'})
    numlist = []
    for num in numbers:
        numlist.append(num.text)
    return numlist


def getting_names():
    soup = web_searcher(sys.argv[1])
    names = soup.find_all('td', {'class': 'overflow_name'})
    namlist = []
    for name in names:
        namlist.append(name.text)
    return namlist


def get_field_names():
    web = web_searcher(FIELS_NAMES)
    final_headers = ['code', 'location', 'registered', 'envelopes', 'valid']
    tables = web.find_all('div', {'class': 't2_470'})
    for line in tables:
        headers = line.find_all('td', {'class': 'overflow_name'})
        for head in headers:
            final_headers.append(head.text)
    return final_headers
    

def extract_data(web):
    codes = ['sa2','sa3','sa6']
    datas = []
    site = web_searcher(web)
    for code in codes:
        datas.append(site.find('td', {'headers':code}).text)
    return datas


def extract_votes(web):
    votes = []
    site = web_searcher(web)
    tables = site.find_all('div', {'class': 't2_470'})
    
    for table in tables:
        headers = table.find_all('td', {'headers': 't1sa2 t1sb3'})
        for head in headers:
            votes.append(head.text)
    for table in tables:
        headers = table.find_all('td', {'headers': 't2sa2 t2sb3'})
        for head in headers:
            votes.append(head.text)   
    return votes


def all_joined_votes(url):
    text = []
    soup = web_searcher(url)
    links = find_links(soup)
    for link in links:
        full_link = MAIN_URL + link
        data = extract_data(full_link)
        votes = extract_votes(full_link)
        text.append(data+votes)
    return text


def joining_num_and_nam():
    main_value = []
    names = getting_names()
    numbers = getting_number()
    for num in range(len(names)):
        side_list = [numbers[num], names[num]]
        main_value.append(side_list)
    return main_value


def file_maker(text):
    if sys.argv[2] in os.listdir():
        mode = 'a'  
    else:
        mode = 'w'
        
    with open(sys.argv[2], mode, encoding="ISO 8859-2", newline='') as f_new:
        field_names = get_field_names()
        printer = csv.writer(f_new)
        if mode == 'w':
            printer.writerow(field_names)
        for item in text:
            printer.writerow(item)
        



def main_function():
    if argument_checker():
        print("stahuji data ze stranky!".upper())
        list1 = joining_num_and_nam()
        list2 = all_joined_votes(sys.argv[1])
        clean_list2 = []
        for items in list2:
            side_list = []
            for item in items:
                side_list.append(item.replace('\xa0', ''))
                if item == '-':
                    clean_list2.append(side_list)
        
        list3 = []
        for i in range(len(list1)):
            list3.append(list1[i] + clean_list2[i])
        file_maker(list3)
        print(f'data ulozena v {sys.argv[2]}'.upper())
        
        


    else:
        print('''
        chybi ti argumenty!!
        1. link na stranku ze ktereho chces cerpat
        2. nazev souboru
        (pouzij "" az budes zadavat nazvy)
        ''')

main_function()