from fastapi import APIRouter, Depends
from rate.dependencies import add_rates_to_db, decode_file, is_json
from rate.models import Rate
from typing import List
from rate.shemas import CalcRateScheme, InputRateScheme, RateScheme

router = APIRouter(prefix="/rate", tags=["Rate"])


@router.get("/all_rate", response_model=List[RateScheme])
async def get_all_rate():
    return await RateScheme.from_queryset(Rate.all())


@router.post("/upload_rates", dependencies=[Depends(is_json)])
async def upload_rates(file: dict = Depends(decode_file)) -> None:
    await add_rates_to_db(file)


@router.post("/get_rate", response_model=RateScheme | None)
async def get_rate(data: InputRateScheme):
    return await RateScheme.from_queryset_single(
        Rate.get(date=data.date, cargo_type=data.cargo_type)
    )


@router.delete("/delete_rate/{date}/{cargo_type}")
async def delete_rate(date: str, cargo_type: str) -> None:
    await Rate.get(date=date, cargo_type=cargo_type).delete()


@router.post("/calc")
async def calc(data: CalcRateScheme) -> float:
    rate = await RateScheme.from_queryset_single(
        Rate.get(date=data.date, cargo_type=data.cargo_type)
    )
    return float(rate.rate) * data.price
