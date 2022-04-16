import pygsheets
import pandas as pd
from app.tools.files import write_to_json, read_from_json

CREDS = './configs/creds.json'  # Type your creds from Google api here


def create_table(name):
    service = pygsheets.authorize(service_file=CREDS)
    spreadsheet = service.create(name)
    write_to_json({'spreadsheetId': spreadsheet.id}, './configs/config.json')


def get_link():
    service = pygsheets.authorize(service_file=CREDS)
    spreadsheet_id = read_from_json('./configs/config.json')['spreadsheetId']
    spreadsheet = service.open_by_key(spreadsheet_id)
    return spreadsheet.url


def get_access(email):
    service = pygsheets.authorize(service_file=CREDS)
    spreadsheet_id = read_from_json('./configs/config.json')['spreadsheetId']
    spreadsheet = service.open_by_key(spreadsheet_id)
    spreadsheet.share(email, 'writer')


def get_data():
    service = pygsheets.authorize(service_file=CREDS)
    spreadsheet_id = read_from_json('./configs/config.json')['spreadsheetId']
    spreadsheet = service.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.sheet1
    return worksheet.get_as_df()


def write_data(data):
    old_data = {}
    old_data.update(get_data().to_dict(orient="list"))
    old_data.update(data)
    new_data = pd.DataFrame(old_data)
    service = pygsheets.authorize(service_file=CREDS)
    spreadsheet_id = read_from_json('./configs/config.json')['spreadsheetId']
    spreadsheet = service.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.sheet1
    worksheet.set_dataframe(df=new_data, start=(1, 1))


if __name__ == "__main__":
    # create_table('Jup.ug')
    # get_access('wyndace@hotmail.com')
    write_data({'huh': [21212, 2121212, 212121, 21211]})
