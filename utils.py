from operator import itemgetter

from Classes import DataBase
from data import resort_list


async def get_top_resort() -> dict:
    database = DataBase()
    dict_resort = {}
    for n, coo in resort_list.items():
        res_data = await database.resort_data(n)
        snowfall = int(sum(res_data.get('snowfall_sum')))
        dict_resort[n] = snowfall
    await database.close()
    return dict(sorted(dict_resort.items(), key=itemgetter(1), reverse=True)[:4])


async def get_list_resort() -> dict:
    database = DataBase()
    dict_resort = {}
    for n, coo in resort_list.items():
        res_data = await database.resort_data(n)
        snowfall = int(sum(res_data .get('snowfall_sum')))
        dict_resort[n] = snowfall
    await database.close()
    return dict_resort
