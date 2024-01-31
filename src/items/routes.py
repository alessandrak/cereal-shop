from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.core.utils import has_intersection
from src.items import schemas, services

items_router = APIRouter(prefix="")


@items_router.post(
    "/cart/calculate-price", response_model=schemas.CalculateCartPriceResponse
)
def calculate_cart_price(
    req: schemas.CalculateCartPriceRequest, db: Session = Depends(get_db)
):
    cart = req.cart
    discount = services.get_discount(db)

    cart_skus = [x.sku for x in cart.line_items]
    cart_items = services.get_items_by_skus(db, skus=cart_skus)

    if has_intersection(discount.prerequisite_items, cart_items) & has_intersection(
        discount.eligible_items, cart_items
    ):
        cart.apply_discount(discount=schemas.Discount.from_orm(discount))

    response = schemas.CalculateCartPriceResponse(
        totalPrice=cart.get_total_price(),
        reference=cart.reference,
        lineItems=cart.line_items,
    )
    return response


@items_router.get("/items/", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = services.get_items(db)
    return items


@items_router.get("/discounts/", response_model=schemas.Discount)
def read_discount(db: Session = Depends(get_db)):
    discount = services.get_discount(db)
    return discount
