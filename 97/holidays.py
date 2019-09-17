from collections import defaultdict
import os
from pprint import pprint
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, features="html.parser")
    table = soup.select('tbody > tr')
    for holiday in table:
        month = (holiday.find('time').text).split("-")[1]
        holiday_name = holiday.find('a').text
        holidays[month].append(holiday_name)
    return holidays
