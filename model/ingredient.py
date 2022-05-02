from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from core.database import Base
from datetime import datetime
from model.base import ModelBase


class Ingredient(ModelBase, Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, description, recipe_id):
        ingrendient = Ingredient()
        ingrendient.description = description
        ingrendient.recipe_id = recipe_id
        session.add(ingrendient)
        session.commit()
        session.refresh(ingrendient)
        return Ingredient.find_by_id(session=session, id=ingrendient.id)