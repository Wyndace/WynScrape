async def async_chooser_menu(inp_text, items):
    choice = -1
    while 0 > choice or choice > items:
        try:
            choice = int(input(inp_text))
        except Exception:
            print('\nВведено неверное значение! Попробуйте ещё раз!\n')
            continue
        if 0 > choice or choice > 4:
            print('\nВведено неверное значение! Попробуйте ещё раз!\n')
    return choice


def chooser_menu(inp_text, items):
    choice = -1
    while 0 > choice or choice > items:
        try:
            choice = int(input(inp_text))
        except Exception:
            print('\nВведено неверное значение! Попробуйте ещё раз!\n')
            continue
        if 0 > choice or choice > 4:
            print('\nВведено неверное значение! Попробуйте ещё раз!\n')
    return choice
