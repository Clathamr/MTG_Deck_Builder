from dataclasses import dataclass
from typing import Optional


@dataclass
class MTGCard:
    id: str
    name: str
    mana_cost: Optional[str]
    cmc: float | None
    colors: list[str]
    type_line: str | None
    rarity: str | None
    text: str | None
    power: str | None
    toughness: str | None
