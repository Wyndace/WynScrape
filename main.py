from asyncio import run
from time import monotonic
from app.states.menu import menu


async def main():
    # Use initialization and main menu functions here
    await menu(scheduler)


if __name__ == '__main__':
    start = monotonic()
    run(main())
    print('Кол-во секунд, которые скрипт работал ->', monotonic() - start)
