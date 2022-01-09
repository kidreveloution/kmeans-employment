from fastapi import FastAPI
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from docheader import getHeader
docHeaderAPI = FastAPI()


@docHeaderAPI.get("/")
async def root():
    return {"message": "Hello World"}



#Here is where the file will be uploaded
@docHeaderAPI.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    #df = pd.read_csv(contents)
    #list_of_column_names = list(df.columns)
    fType = contents

    #headers = getHeader(contents)
    return {"filename": file.filename,
            "fileType": fType}
