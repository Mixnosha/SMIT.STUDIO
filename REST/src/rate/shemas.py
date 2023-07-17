from datetime import datetime
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from rate.models import Rate

RateScheme = pydantic_model_creator(Rate, name="Rate")


class InputRateScheme(BaseModel):
    date: str = Field("2020-12-24")
    cargo_type: str = Field("Glass")


class CalcRateScheme(InputRateScheme):
    price: float = Field(1.1)
