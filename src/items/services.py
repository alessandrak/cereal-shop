from sqlalchemy.orm import Session

from src.core import models


def get_discount(db: Session) -> models.Discount:
    return db.query(models.Discount).options().first()


def get_items(db: Session) -> list[models.Item]:
    return db.query(models.Item).all()


def get_items_by_skus(db: Session, skus: list[str]) -> list[models.Item]:
    return db.query(models.Item).filter(models.Item.sku.in_(skus)).all()
