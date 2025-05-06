import gspread
from gspread import utils 
from google.oauth2.service_account import Credentials
from datetime import datetime as dT
from multipledispatch import dispatch
import re


scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
#downloaded credentials created from googleAPI
creds = Credentials.from_service_account_file('credentials.json', scopes = scopes)
client = gspread.authorize(creds)

#Sheet ID is the string right before the /edit
sheet_id = ""
sheet = client.open_by_key(sheet_id)

#Choose Latest Worksheet by index -2 as I have a Blueprint Sheet
worksheet = sheet.get_worksheet(-2)

avg_formula = '=ROUND(AVERAGE({}),2)'

def get_row_of(date):
    row = worksheet.find(dT.strftime(date, '%d/%m/%Y')).row
    return row

def set_calories(date, list_cals):
    row = get_row_of(date)
    formula = avg_formula.format(','.join(list_cals))
    worksheet.update_cell(row,1,formula)


