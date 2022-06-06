from pydantic import BaseModel

class TermoResponse(BaseModel):
    temperature: float
    chimney:float
    distance:int
