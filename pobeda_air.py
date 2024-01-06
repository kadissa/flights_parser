from pyairports.airports import Airports

from airports_airlines import *


def get_date(i):
    if i < 10:
        return f'&date%5B0%5D=0{i}.01.2024'
    return f'&date%5B0%5D={i}.01.2024'


BASE_URL = 'https://ticket.pobeda.aero/websky/?'
dispatch = f'origin-city-code%5B0%5D={AIRPORT_CODES["СПБ"]}'
arrive = f'&destination-city-code%5B0%5D={AIRPORT_CODES["Сочи"]}'
dates_interval = range(10, 30)
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
