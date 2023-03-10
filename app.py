from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/api/sunset")
async def root():
  return {
      "sunset": "2023-03-10T15:27:00.000000"
  }