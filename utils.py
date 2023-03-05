from operator import itemgetter

import requests

from data import resort_list


def req_resort_datas(coord: list[float]) -> dict:
    lat, log = coord
    req = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={log}&daily=temperature_2m_max,' \
          f'temperature_2m_min,snowfall_sum,precipitation_probability_max&timezone=Europe%2FMoscow&past_days=3'
    res = requests.get(req)
    return res.json().get('daily')


def get_top_resort():
    dict_resort_snowfall = {n: int(sum(req_resort_datas(coo).get('snowfall_sum'))) for n, coo in resort_list.items()}
    return dict(sorted(dict_resort_snowfall.items(), key=itemgetter(1), reverse=True)[:4])


def get_list_resort():
    return {n: int(sum(req_resort_datas(coo).get('snowfall_sum'))) for n, coo in resort_list.items()}
