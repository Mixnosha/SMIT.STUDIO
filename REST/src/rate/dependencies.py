from datetime import datetime
import json
from typing import List
from fastapi import HTTPException, UploadFile, status
from rate.models import Rate


def to_date(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return date_obj.date()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid date. Valid format YYYY-MM-DD",
        )


async def add_rates_to_db(data: dict) -> List[Rate] | None:
    for k, v in data.items():
        date = to_date(k)
        try:
            to_db = [
                Rate(date=date, cargo_type=obj["cargo_type"], rate=obj["rate"])
                for obj in v
            ]
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file structure.",
            )

        await Rate.bulk_create(
            to_db, update_fields=("rate",), on_conflict=("date", "cargo_type")
        )


def is_json(file: UploadFile) -> None:
    filename = file.filename
    if not filename.endswith(".json"):
        raise HTTPException(status_code=status.HTTP_410_GONE, detail="Only .json file")


async def decode_file(file: UploadFile) -> dict:
    try:
        data = json.loads(await file.read())
        return data
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_410_GONE, detail="Invalid json format"
        )
