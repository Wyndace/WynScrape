from pprint import pprint
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

URL = 'https://example.com'
INFO = []


def get_page(browser: uc.Chrome, link: str, is_next: bool) -> None:
    try:
        if not is_next:
            browser.get(URL + link)
    except Exception:
        pass


def parse() -> list[dict]:
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    browser = uc.Chrome(options=options)
    browser.implicitly_wait(30)
    try:
        get_page(browser, f'write part after "/" here')
    except Exception as e:
        print(e)
    finally:
        browser.close()
        return INFO


if __name__ == "__main__":
    parse()
