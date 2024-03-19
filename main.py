import mysql.connector
import requests
from bs4 import BeautifulSoup
import sys
import datetime

# Set the encoding of the output stream to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# MySQL database configuration
db_config = {
    'user': '####',
    'password': '####',
    'host': '####',
    'database': 'poke_data',
}

# Create a MySQL connection
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# Iterate over each page
for page_number in range(2, 12):
    url = f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=grade+10+pokemon+card&_sacat=0&LH_TitleDesc=0&rt=nc&_odkw=grade+10+pokemon+card&_osacat=0&LH_BIN=1&_ipg=240&_pgn={page_number}"

    # Get raw data function
    def get_data(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup

    # parse page data function
    def parse(soup):
        results = soup.find_all("div", {"class": "s-item__info clearfix"})
        for item in results:
            name = item.find("div", {"class": "s-item__title"}).text
            price = item.find("span", {"class": "s-item__price"}).text
            link = item.find("a", {"class": "s-item__link"})["href"]
            postageCost = str(
                item.find("span", {"s-item__shipping s-item__logisticsCost"}))
            dateQueried = datetime.datetime.now().isoformat()

            # Insert the data into the MySQL database
            insert_query = "INSERT INTO ebay_raw_data (name, price, link, postage_cost, dateQueried) VALUES (%s, %s, %s, %s, %s)"
            values = [(name, price, link, postageCost, dateQueried)]

            cursor.executemany(insert_query, values)
            cnx.commit()

    soup = get_data(url)
    parse(soup)

# Close the MySQL connection
cursor.close()
cnx.close()
