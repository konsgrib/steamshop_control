from typing import Optional

from fastapi import FastAPI

from termo import read_temp, read_max

from sonar import get_distance

from schemas.termo import TermoResponse

app = FastAPI()


@app.get('/temperature',response_model=TermoResponse)
def get_temperature():
    return {
        'temperature': read_temp(),
        'chimney': read_max(),
        'distance': get_distance()
    }

if __name__ == "__main__":
    # get_temperature()
    print(read_temp())
    # print( read_max())
    print(get_distance())