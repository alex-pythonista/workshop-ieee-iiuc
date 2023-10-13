from enum import Enum
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

class Country(Enum):
    JAPAN = "JP"
    BANGLADESH = "BD"
    USA = "USA"


@app.get("/say_hello/{country}")
async def hello(
    country: Country
):
    res = {}
    print(country)
    if country == Country.JAPAN:
        res["greet"] = "こんにちは"
    elif country == Country.BANGLADESH:
        res["greet"] = "হ্যালো"
    else:
        res["greet"] = "Hello"
    return JSONResponse(
        content=res
    )
