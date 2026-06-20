from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)  # TODO: dont use plaintext

    cards = relationship("Card", back_populates="user")
    decks = relationship("Deck", back_populates="user")


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="cards")
    mtg_api_id = Column(String)
    quantity = Column(Integer, default=1)

    users = relationship("User", back_populates="cards")


class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)

    users = relationship("User", back_populates="decks")
    cards = relationship("Card", back_populates="decks")


class DeskCard(Base):
    __tablename__ = "deck_cards"
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey("decks.id"))
    card_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)

    decks = relationship("Deck", back_populates="cards")
