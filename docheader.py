
import pandas as pd
from fastapi import FastAPI, File, UploadFile


async def getHeader(file):
    df = pd.read_csv(file)
    list_of_column_names = list(df.columns)

    print('List of column names : ',
        list_of_column_names)
