from httpx import Client
from typing import Any
from selectolax.parser import HTMLParser, Node
from re import search as regex_search

from .connector import Connector
from ...config import urls


def get_item_text(block: Node | HTMLParser, selector: str = '',
                  deep: bool = True) -> str:
    try:
        if selector:
            return block.css_first(selector).text(deep=deep)\
                .replace('\xa0', ' ').strip()
        return block.text(deep=deep).replace('\xa0', '').strip()
    except AttributeError as e:
        return ""


def get_item_attribute(block: Node | Any,
                       attribute: str, selector: str = '') -> str | None:
    try:
        if selector:
            return block.css_first(selector).attributes.get(attribute)
        return block.attributes.get(attribute)
    except AttributeError:
        return None


def get_value_from_regex(regex: str, string: str | None) -> str:
    if not string:
        return ""
    regex_result = regex_search(regex, string)
    if regex_result:
        return regex_result.group()
    else:
        return ""


def get_html(client: Client, url: str) -> str | None:
    r = Connector.get(client, url)
    if r:
        return r.text


def get_heading(raw_html: str) -> str:
    html = HTMLParser(raw_html)
    heading_text = get_item_text(html, "css")
    return heading_text


def run():
    # test function
    ...


if __name__ == "__main__":
    run()
