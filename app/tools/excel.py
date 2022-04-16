from pprint import pprint

from openpyxl import load_workbook
import pandas as pd

from app.tools.files import delete_path


def add_excel(row, path, table) -> None:
    wb = load_workbook(path)
    ws = wb[table]
    ws.append(row)
    wb.save(path)
    wb.close()


def get_table(path: str = './xlsx/result.xlsx'):
    xl = pd.ExcelFile(path, engine='openpyxl')
    d = xl.parse("Main")
    return d


def clear_table(extra_names: dict = None, path: str = './xlsx/result.xlsx', lock: bool = False, delete: bool = True):
    if extra_names is None:
        extra_names = {}
    if lock:
        pass
    else:
        if delete:
            delete_path(path)
        pd.set_option('max_colwidth', 100000)
        writer = pd.ExcelWriter(path, engine='openpyxl')
        names = {}
        names.update(extra_names)
        first_row = pd.DataFrame(names)
        first_row.to_excel(writer, sheet_name='Main', index=False)
        writer.save()


def update_table(data: dict, path: str = './xlsx/result.xlsx'):
    old_data = get_table().to_dict(orient="list")
    old_data.update(data)
    clear_table(extra_names=old_data, delete=False)