from pprint import pprint
from requests import Session

URL = 'https://example.com'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "*"
}
INFO = []


def get_data(session, link):
    with session.get(url=URL + link, headers=HEADERS) as req:
        # write your parsing code here
        pass


def get_page():
    session = Session()
    get_data(session, 'write the next part after / here')


def parse():
    get_page()


if __name__ == "__main__":
    parse()
    pass
