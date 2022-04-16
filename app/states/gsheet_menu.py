from asyncio import run

from app.tools import gsheet
from app.tools.common import async_chooser_menu


async def gsheet_menu():
    while True:
        inp_text = '''Выберите пункт меню настройки импорта в гугл таблицы:
            1.) Получить ссылку на таблицу
            2.) Получить доступ к таблице
            3.) Выйти в главное меню

Ваш выбор: '''
        choice = await async_chooser_menu(inp_text, 3)
        if choice == 1:
            print(f'Ссылка на гугл таблицу ->  {gsheet.get_link()}')
        elif choice == 2:
            email = input('Напишите ваш email с которого Вы будете заходить в таблицу: ')
            gsheet.get_access(email)
            print('Доступ получен!')
        elif choice == 3:
            return choice

if __name__ == '__main__':
    while True:
        run(gsheet_menu())
