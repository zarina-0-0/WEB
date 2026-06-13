from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


temp_bd = [
{
    "id": 1,
    "category": "силовая",
    "tittle": "пресс + руки",
    "date": "2026-04-22",
    "duration": 25,
    "user": {
        "id": 1,
        "name": "Зарина Биктагирова",
        "level": 3
    },
    "notes": "тренировка прошла легко но сильно вспотела)",
    "exercises":
        [{
            "id": 1,
            "name": "планка",
            "sets": 3,
            "reps": None,
            "duration": 40,
            "weight": None,
            "description": "четыре опоры на руках и ногах, руки под плечами, поясница не проваливается и не поднимается высоко"

        },
        {
            "id": 2,
            "name": "отжимания",
            "sets": 3,
            "reps": 8,
            "duration": None,
            "weight": None,
            "description": ""

        }]
},
{
    "id": 2,
    "category": "силовая",
    "tittle": "ноги",
    "date": "2026-05-22",
    "duration": 25,
    "user": {
        "id": 1,
        "name": "Даша",
        "level": 2
    },
    "notes": "устала, но не сильно",
    "exercises":
        [{
            "id": 1,
            "name": "выпады с гантелями",
            "sets": 3,
            "reps": 15,
            "duration": None,
            "weight": 6,
            "description": "спина прямая, угол в коленях 90 градусов"

        }]
},]