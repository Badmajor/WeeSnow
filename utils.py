import json
from operator import itemgetter

from classes import DataBase, req_resort_datas
from data import resort_list


def get_top_resort() -> dict:
    database = DataBase()
    dict_resort = {}
    for n, coo in resort_list.items():
        snowfall = sum(database.resort_data(n).get('snowfall_sum'))
        dict_resort[n] = snowfall
    database.close()
    return dict(sorted(dict_resort.items(), key=itemgetter(1), reverse=True)[:4])


def get_list_resort() -> dict:
    database = DataBase()
    dict_resort = {}
    for n, coo in resort_list.items():
        snowfall = sum(database.resort_data(n).get('snowfall_sum'))
        dict_resort[n] = snowfall
    database.close()
    return dict_resort


