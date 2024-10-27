from typing import List

from pydantic import BaseModel


class TermoResponse(BaseModel):
    temperature: float
    chimney: float
    distance: int


class Sensor(BaseModel):
    id: str
    name: str
    type: str
    address: str
    temperature: float


class SensorList(BaseModel):
    sensors: List[Sensor]
