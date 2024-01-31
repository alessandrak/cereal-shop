from pydantic import BaseModel, Field

from src.core.models import DiscountUnit


class Item(BaseModel):
    sku: str

    class Config:
        orm_mode = True


class ItemCreate(Item):
    eligible_for_id: int | None = None
    prerequisite_for_id: int | None = None


class ItemList(Item):
    name: str
    price: float


class Discount(BaseModel):
    discount_unit: DiscountUnit
    discount_value: float
    prerequisite_items: list[Item] = []
    eligible_items: list[Item] = []

    class Config:
        orm_mode = True

    def apply_discount_to_item(self, item: Item):
        if self.discount_unit == DiscountUnit.percentage:
            item.price = item.price * (100 - self.discount_value) / 100


class Cart(BaseModel):
    reference: str
    line_items: list[ItemList] = Field(alias="lineItems")

    def sort_items_by_price(self):
        self.line_items = sorted(self.line_items, key=lambda x: x.price)

    def get_total_price(self):
        return round(sum([item.price for item in self.line_items]), 2)

    def apply_discount(self, discount: Discount):
        self.sort_items_by_price()
        eligible_skus = [x.sku for x in discount.eligible_items]
        for item in self.line_items:
            if item.sku in eligible_skus:
                discount.apply_discount_to_item(item)
                return


class CalculateCartPriceRequest(BaseModel):
    cart: Cart


class CalculateCartPriceResponse(Cart):
    total_price: float = Field(alias="totalPrice")
