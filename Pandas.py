import pandas as pd
from datetime import datetime, timedelta
from csv import reader

drugs = 'excelfilename'
df_drugs = pd.read_csv(drugs)

df_drugs['side effects'] = pd.to_da