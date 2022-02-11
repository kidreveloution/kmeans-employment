from fastapi import FastAPI, File, UploadFile
from docheader import getHeader
import shutil
docHeaderAPI = FastAPI()


@docHeaderAPI.get("/")
async def root():
    return {"message": "Hello World"}



@docHeaderAPI.post("/uploadfile/")
async def create_upload_file(imported: UploadFile = File(...)):
    with open(f'{imported.filename}', "wb") as buffer:
        shutil.copyfileobj(imported.file, buffer)
        headers = getHeader(str(buffer.name))
    return {"filename": imported.filename,
            "Headers": headers}
