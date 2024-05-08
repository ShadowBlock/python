"""
BeutifulSoap kood magaziin.ee lehe jalanõude scrapimiseks.
"""
import requests
from bs4 import BeautifulSoup
import json
import time

# Data listi tegemine ja urlid
start_url = 'https://pood.magaziin.ee/product-category/jalatsid/'
base_url = 'https://pood.magaziin.ee'
data_list = []


# Alustab scrapimist
def parse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Produkti class
    products = soup.find_all("li", class_='product')

    for jalatsid in products:
        product_data = {'Title': '', 'Price': '', 'Picture href': ''}

        # Nimi, hind ja pildi href
        product_data['Title'] = jalatsid.find('h2', class_='woocommerce-loop-product__title').text
        price_with_euro_symbol = jalatsid.find('span', class_='woocommerce-Price-amount').bdi.text
        product_data['Price'] = price_with_euro_symbol.replace('\u20ac', '')
        product_data['Picture href'] = jalatsid.find('img')['src']

        data_list.append(product_data)

    # Järgmisele lehele minemine
    try:
        next_page = soup.find("a", class_='next')['href']
        if next_page:
            next_url = base_url + next_page
            print("Going to next page.")
            time.sleep(5)
            parse(next_url)
    except:
        print("No more pages.")


if __name__ == '__main__':
    print("Starting scraping page.")
    parse(start_url)

    # Teeme kogu data JSON failiks, kindlustame selle, et faili formaat oleks sama mis scrapy omal.
    with open('soap_output_magaziin.json', 'w') as json_file:
        json_file.write("[\n")
        for i, data in enumerate(data_list):
            if i > 0:
                json_file.write(",\n")
            json.dump(data, json_file)
        json_file.write("\n]")
