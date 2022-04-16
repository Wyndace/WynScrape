from apscheduler.schedulers.background import BackgroundScheduler

from app.tools.parser import get_page

URL = 'https://example.com'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "*"
}
INFO = []


def background_parsing(scheduler: BackgroundScheduler, properties=None):
    if len(properties) > 0:
        scheduler.add_job(func=get_page, args=[properties], trigger='interval', seconds=60,
                          id=f'id')
        # scheduler.print_jobs()
        print(f'Запущен парсер id')


async def background_parsing_deleter(scheduler: BackgroundScheduler, properties=None):
    scheduler.remove_job('id')
    print(f'Удалён парсер id')
