#this only updates first row not the entire datagrame don't know why
#this is just a skeleton to approach the main problem
import pandas as pd
import gspread
import df2gspread as d2g
from google.oauth2.service_account import Credentials
import gspread_dataframe as gd


path = "Songs_LA - Sheet1.csv"
database = pd.read_csv(path)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = Credentials.from_service_account_file('creds.json').with_scopes(scope)

gc = gspread.authorize(credentials)

spreadsheet_key = '18FGghQub2BPeMB2BUsRtwgpTRymmfxXIc2E7dpj_uAw'
wks_name = 'Master'
# d2g.upload(database, spreadsheet_key, wks_name, credentials=credentials, row_names=True)

ws = gc.open("testSheet").worksheet("Sheet1")
existing = gd.get_as_dataframe(ws)
updated = existing.append(database)
gd.set_with_dataframe(ws, updated)
