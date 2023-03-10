import json
import sqlite3
import datetime
import requests

from data import resort_list


curr_date = datetime.datetime.now()


def req_resort_datas(coord: list[float]) -> dict:
    lat, log = coord
    req = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={log}&daily=' \
          f'temperature_2m_min,snowfall_sum&timezone=Europe%2FMoscow&past_days=3'
    res = requests.get(req)
    return res.json().get('daily')


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('resorts_data.db')
        self.cur = self.conn.cursor()
        self.data = self.cur.execute("CREATE TABLE IF NOT EXISTS data(datetime TEXT, resort TEXT, data TEXT)")
        self.conn.commit()

    def last_update(self) -> bool:
        """Проверяет прошло ли 3 часа с прошлого обновления, возвращает True - если прошло"""
        # получаем из базы
        try:
            self.cur.execute("SELECT datetime FROM data")
            timestamp = str(self.cur.fetchone()[0])
            datetime_obj_timestamp = datetime.datetime.strptime(timestamp, '%y-%m-%d %H:%M:%S')
            return curr_date - datetime.timedelta(hours=3) > datetime_obj_timestamp
        except (TypeError, ValueError) as ex:
            print('Ошибка:', ex)
            return True

    def update_data(self):
        self.cur.execute("DELETE FROM data")
        date = curr_date.strftime('%y-%m-%d %H:%M:%S')
        print('date:',date)
        for n, coo in resort_list.items():
            self.cur.execute("INSERT INTO data(datetime, resort, data) VALUES(?,?,?)",
                             (date, n, str(req_resort_datas(coo))))
        self.conn.commit()

    def resort_data(self, resort: str):
        """Возвращает данные ГЛК по названию"""
        if self.last_update():
            print('lastupdate:', True)
            self.update_data()
        self.cur.execute("SELECT * FROM data WHERE resort = ?", (resort,))
        ans_str = self.cur.fetchone()[2]
        ans_dict = json.loads(ans_str.replace("'", '"'))
        return ans_dict

    def close(self):
        self.conn.close()
