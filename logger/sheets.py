import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def auth(credpath, sheetname):
    ''' credpath
        Path to the credentials.json file used
        for authorization, can be downloaded from
        https://console.developers.google.com/apis/credentials

        sheetname
        Name of the sheet where the data will be entered.
        This needs to be shared with the email address
        specified in credentials.json.

    Authorizes user with the google drive api using credentials.json
    and opens the spreadsheet <sheetname> as a Worksheet object stored
    in the global variable <sheet>'''
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credpath = os.path.abspath(credpath)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credpath, scope)
    client = gspread.authorize(credentials)
    global sheet
    sheet = client.open('data').worksheet("Maltes Paj")


def write(data):
    ''' data
        List of values or strings

    Writes each item in <data> as separate
    cells on a new row to the sheet 
    previously opened using auth().
    This sheet is the Worksheet object stored in the global variable <sheet>'''
    sheet.append_row(data)
