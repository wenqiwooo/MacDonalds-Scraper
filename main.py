import re
import time
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver


PHANTOMJS_PATH = 'bin/phantomjs'


def open_url(brower, zipcode):
  url = 'https://www.mcdonalds.com/us/en-us/restaurant-locator.html?submit=true&radiusSelected=5&searchText={}#rl-listView'.format(zipcode)
  browser.get(url)
  time.sleep(20)
  bs_obj = BeautifulSoup(browser.page_source, 'html.parser')
  for item in bs_obj.findAll(attrs={'id': re.compile(r'^restaurant-location-list-')}):
    title = item.find(attrs={'class': 'restaurant-location__title'}).get_text()
    address = item.find(attrs={'class': 'restaurant-location__address'}).get_text()
    print '{} {}'.format(title, address)


if __name__ == '__main__':
  browser = webdriver.PhantomJS(PHANTOMJS_PATH, service_args=['--ignore-ssl-errors=true'])
  zipcode = raw_input('What zipcode are you at?\n')
  print('Scraping for data...')
  open_url(browser, zipcode)
