from mtgsdk import Card

"""This function queries https://api.magicthegathering.io/v1/cards to return a Card object using the name provided
as an argument, or return None if no card is found. If multiple cards are found, a list is returned by the api and
this function returns the first element in the list.

API docs available at: https://docs.magicthegathering.io/?utm_source=freeapihub.com&utm_medium=referral#api_v1cards_get
"""


def get_card_by_name(search_name) -> Card | None:
    sourced_cards = Card.where(name=search_name).all()

    if not sourced_cards:
        # print(f"{search_name} not found")
        return None

    card = sourced_cards[0]  # TODO: consider a better approach for searching cards

    # print(card.name)
    return card


# get_card_by_name("")
