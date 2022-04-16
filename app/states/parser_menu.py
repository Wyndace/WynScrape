from asyncio import run

from app.tools.async_parser import background_parsing, background_parsing_deleter
from app.tools.common import async_chooser_menu
from app.tools.parser import parse


async def parser_menu(*args):
    while True:
        inp_text = '''Выберите пункт меню управления парсером:
            1.) Вывести единоразового результат парсинга
            2.) Добавить задачу парсинга
            3.) Удалить задачу парсинга 
            4.) Выйти в главное меню

Ваш выбор: '''
        choice = await async_chooser_menu(inp_text, 4)
        if choice == 1:
            parse()
        elif choice == 2:
            background_parsing(args[0])
        elif choice == 3:
            await background_parsing_deleter(args[0])
        elif choice == 4:
            return choice

if __name__ == '__main__':
    while True:
        run(parser_menu())
