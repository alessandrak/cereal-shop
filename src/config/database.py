from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./cereal-shop.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

def create_objects(db: Session):
    from src.core import models
    from src.items import schemas
    
    discount = models.Discount(discount_unit="percentage", discount_value=50.0)
    db.add(discount)
    db.commit()

    skus = ["PEANUT-BUTTER", "COCOA", "FRUITY", "BANANA-CAKE", "CHOCOLATE"]
    prerequisite_items = ["PEANUT-BUTTER", "COCOA", "FRUITY"]
    elegible_items = ["BANANA-CAKE", "COCOA", "CHOCOLATE"]
    for sku in skus:
        item = schemas.ItemCreate(sku=sku)
        if sku in elegible_items:
            item.eligible_for_id = discount.id
        if sku in prerequisite_items:
            item.prerequisite_for_id = discount.id
        db.add(models.Item(**item.dict()))

    db.commit()
    