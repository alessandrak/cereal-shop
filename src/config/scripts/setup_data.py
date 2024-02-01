import sys

from src.config.database import Base, engine, get_db
from src.core import models
from src.items import schemas


# PRO: Seed database, nice!!
def main():
    db = next(get_db())
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create discount
    discount = models.Discount(
        discount_unit=models.DiscountUnit.percentage, discount_value=50.0
    )
    db.add(discount)
    db.commit()

    # Create items
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


if __name__ == "__main__":
    main()
    print("Data created")
    sys.exit(0)
