from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/mex")
async def mexico():
    return {"message": "Its raining mexic"}
