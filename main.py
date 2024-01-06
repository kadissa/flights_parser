"""
Делает запрос к сайту <Победы>
из аэропорта {dispatch}
в аэропорт {arrive}
на даты, указанные в {dates_interval}
и возвращает минимальную цену рейса на эту дату.
"""
import time

from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pobeda_air import *

if __name__ == '__main__':
    flights = []
    for _ in dates_interval:
        request = BASE_URL + dispatch + arrive + get_date(_) + TAIL_URL
        session = HTMLSession()
        response = session.get(request)
        response.html.render(sleep=3)
        # response.html.render(scrolldown=1)

        soup = BeautifulSoup(response.html.html, features='lxml')
        div = soup.find('div', {'class': 'chooseFlight__list__item__content'})
        div_price = div.find(
            'div',
            {'class': 'chooseFlight__list__item__content__info__price'}
        )
        price = div_price.find(
            'span', {
                'ng-bind-html':
                    '{ value: row.minPrice, currency: '
                    'row.minPriceCurrency } | price'
            }
        )
        flights.append(f'{airport_departure.name}-{airport_arrival.name}\n'
                       f'{get_date(_).split("=")[-1]}\n'
                       f'{price.text}')
        print(f'{airport_departure.name}-{airport_arrival.name}\n'
              f'{get_date(_).split("=")[-1]}\n'
              f'{price.text}')
        time.sleep(3)
    print('---------------------------------')
    print(*flights)
