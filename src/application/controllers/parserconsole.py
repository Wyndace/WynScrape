from httpx import Client
from ..web import parser
from ...config import urls
from icecream import ic


def print_heading_to_console():
    client = Client()
    raw_html = parser.get_html(client, urls.HTTPS_BASE)
    if raw_html:
        heading = parser.get_heading(raw_html)
        ic(heading)
