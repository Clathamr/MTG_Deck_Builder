from app.domain.models import MTGCard


def to_mtg_card(card) -> MTGCard:
    return MTGCard(
        id=card.id,
        name=card.name,
        mana_cost=card.mana_cost,
        cmc=card.cmc,
        colors=card.colors,
        type_line=card.type,
        rarity=card.rarity,
        text=card.text,
        power=card.power,
        toughness=card.toughness,
    )
