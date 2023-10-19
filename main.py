from src.application.utils import menu
from src.application import controllers


def main():
    items = (
        "Показать заголовок страницы example.com",
    )
    choice = menu.multi_chooser_menu("Выберите пункт меню: ", items)
    if choice == 1:
        controllers.parserconsole()


if __name__ == "__main__":
    main()
