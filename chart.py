import matplotlib.pyplot as plt
from io import BytesIO

from aiogram import types

from Classes import DataBase

plt.set_loglevel('WARNING')


async def get_picture(name_resort: str = 'Аджигардак'):
    database = DataBase()
    df = await database.resort_data(name_resort)
    await database.close()

    date = df['time']
    temp_min = df['temperature_2m_min']
    snowfall = df['snowfall_sum']

    fig = plt.figure(figsize=(15, 10), dpi=80)

    ax_main = fig.add_subplot(2, 1, 1)
    ax_bottom = fig.add_subplot(2, 1, 2)

    ax_main.set(title='Температура, С')
    ax_bottom.set(title='Снег , см')
    ax_bottom.set_ylim([0, 50])

    ax_main.grid()
    ax_bottom.grid()
    ax_main.plot(date, temp_min)
    ax_bottom.bar(date, snowfall)

    bio = BytesIO()
    bio.name = f'graf.png'
    plt.savefig(bio)
    bio.seek(0)
    return types.BufferedInputFile(file=bio.getvalue(), filename='graf.png')
