import enum

from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.config.database import Base


class DiscountUnit(enum.Enum):
    percentage = "percentage"


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    sku = Column(String(50), index=True, unique=True, nullable=False)
    prerequisite_for_id = Column(Integer, ForeignKey("discount.id"), nullable=True)
    eligible_for_id = Column(Integer, ForeignKey("discount.id"), nullable=True)

    prerequisite_for = relationship(
        "Discount",
        back_populates="prerequisite_items",
        foreign_keys=[prerequisite_for_id],
    )
    eligible_for = relationship(
        "Discount", back_populates="eligible_items", foreign_keys=[eligible_for_id]
    )


class Discount(Base):
    __tablename__ = "discount"

    id = Column(Integer, primary_key=True)
    discount_unit = Column(Enum(DiscountUnit), nullable=False)
    discount_value = Column(Float, nullable=False)

    prerequisite_items = relationship(
        "Item",
        foreign_keys="Item.prerequisite_for_id",
        back_populates="prerequisite_for",
    )
    eligible_items = relationship(
        "Item", foreign_keys="Item.eligible_for_id", back_populates="eligible_for"
    )
