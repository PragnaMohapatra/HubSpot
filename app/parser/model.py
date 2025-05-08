from dataclasses import dataclass
from typing import List
import requests
import json

@dataclass
class Product:
    id: int
    title: str
    description: str
    price: float
    brand: str
    images: List[str]

def parse_product(data: dict) -> Product:
    return Product(
        id=data['id'],
        title=data['title'],
        description=data['description'],
        price=data['price'],
        brand=data.get('brand','Unknown'),
        images=data.get('images', [])
    )

