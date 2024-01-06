import time
from pprint import pprint
from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests_html
from pyairports.airports import Airports
from bs4 import BeautifulSoup

from airports_airlines import *


def get_date(i):
    if i < 10:
        return f'&date%5B0%5D=0{i}.01.2024'
    return f'&date%5B0%5D={i}.01.2024'

PAUSE_DURATION_SECONDS = 4
BASE_URL = 'https://flysmartavia.com/search/LED-1001-AER-1'
dispatch = f'origin-city-code%5B0%5D={AIRPORT_CODES["СПБ"]}'
arrive = f'&destination-city-code%5B0%5D={AIRPORT_CODES["Сочи"]}'
dates_interval = range(1, 11)
airports = Airports()
airport_departure = airports.airport_iata(
    dispatch.split('=')[-1]
    # 'LED'
)
airport_arrival = airports.airport_iata(arrive.split('=')[-1])

TAIL_URL = (
    '&segmentsCount=1&adultsCount=1&youngAdultsCount=0&childrenCount=0'
    '&infantsWithSeatCount=0&infantsWithoutSeatCount=0&lang=ru#/search'
)

if __name__ == '__main__':
    # Проверка и установка (или обновление) драйвера для Chrome через
    # DriverManager.
    service = Service(executable_path=ChromeDriverManager().install())
    # Запуск веб-драйвера для Chrome.
    driver = webdriver.Chrome(service=service)

    # Открытие страницы по заданному адресу.
    driver.get(BASE_URL)
    # Развёртывание окна на полный экран.
    # driver.maximize_window()
    # Здесь и далее паузы, чтобы рассмотреть происходящее.
    # time.sleep(PAUSE_DURATION_SECONDS)
    # cal = driver.find_element(By.TAG_NAME, 'span')
    h_wrapper = driver.find_element(By.CLASS_NAME, 'calendar-h-wrapper')
    span_day = h_wrapper.find_element(By.CLASS_NAME, 'day-label ')
    # response = session.get(BASE_URLby_class_name)
    # response.html.render(sleep=3)
    soup = BeautifulSoup(driver.page_source, features='lxml')
    div = soup.find('span', {'class': 'day-label'})
    #
    # button_wrapper = div.find('div', {'class': 'button-wrapper'})
    # button = s.find('button', {
    #     'class':
    #     'button extra-large full js-toggle-trigger-custom js-drawer-brands-trigger'
    # })
    # span = button_wrapper.find('span', {'class': 'price nowrap'})
    # cal = div.find('div', {'class': 'calendar-h'})
    # a = soup.find_all('a')
    # print(soup.prettify())
    pprint(div)
    print(span_day.text)
