import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

CALCULATE_CART_PRICE_SUCCESSFULLY_DATA = [
    (
        {
            "cart": {
                "reference": "2d832fe0-6c96-4515-9be7-4c00983539c1",
                "lineItems": [
                    {"name": "Peanut Butter", "price": "39.0", "sku": "PEANUT-BUTTER"},
                    {"name": "Fruity", "price": "34.99", "sku": "FRUITY"},
                    {"name": "Chocolate", "price": "32", "sku": "CHOCOLATE"},
                ],
            }
        },
        {
            "reference": "2d832fe0-6c96-4515-9be7-4c00983539c1",
            "lineItems": [
                {"sku": "CHOCOLATE", "name": "Chocolate", "price": 16.0},
                {"sku": "FRUITY", "name": "Fruity", "price": 34.99},
                {"sku": "PEANUT-BUTTER", "name": "Peanut Butter", "price": 39.0},
            ],
            "totalPrice": 89.99,
        },
    ),
    (
        {
            "cart": {
                "reference": "2d832fe0-6c96-4515-9be7-4c00983539c2",
                "lineItems": [
                    {"name": "Peanut Butter", "price": "39.0", "sku": "PEANUT-BUTTER"},
                ],
            }
        },
        {
            "reference": "2d832fe0-6c96-4515-9be7-4c00983539c2",
            "lineItems": [
                {"sku": "PEANUT-BUTTER", "name": "Peanut Butter", "price": 39.0},
            ],
            "totalPrice": 39.0,
        },
    ),
    (
        {
            "cart": {
                "reference": "2d832fe0-6c96-4515-9be7-4c00983539c3",
                "lineItems": [
                    {"name": "Banana Cake", "price": "35.90", "sku": "BANANA-CAKE"},
                ],
            }
        },
        {
            "reference": "2d832fe0-6c96-4515-9be7-4c00983539c3",
            "lineItems": [
                {"sku": "BANANA-CAKE", "name": "Banana Cake", "price": 35.9},
            ],
            "totalPrice": 35.9,
        },
    ),
    (
        {
            "cart": {
                "reference": "2d832fe0-6c96-4515-9be7-4c00983539c4",
                "lineItems": [
                    {"name": "Cocoa", "price": "37.0", "sku": "COCOA"},
                    {"name": "Banana Cake", "price": "35.90", "sku": "BANANA-CAKE"},
                    {"name": "Fruity", "price": "34.99", "sku": "FRUITY"},
                    {"name": "Chocolate", "price": "32", "sku": "CHOCOLATE"},
                ],
            }
        },
        {
            "reference": "2d832fe0-6c96-4515-9be7-4c00983539c4",
            "lineItems": [
                {"sku": "CHOCOLATE", "name": "Chocolate", "price": 16.0},
                {"sku": "FRUITY", "name": "Fruity", "price": 34.99},
                {"sku": "BANANA-CAKE", "name": "Banana Cake", "price": 35.9},
                {"sku": "COCOA", "name": "Cocoa", "price": 37.0},
            ],
            "totalPrice": 123.89,
        },
    ),
    (
        {
            "cart": {
                "reference": "2d832fe0-6c96-4515-9be7-4c00983539c5",
                "lineItems": [
                    {"name": "Banana Cake", "price": "35.90", "sku": "BANANA-CAKE"},
                    {"name": "Banana Cake", "price": "35.90", "sku": "BANANA-CAKE"},
                    {"name": "Cocoa", "price": "37.0", "sku": "COCOA"},
                    {"name": "Fruity", "price": "34.99", "sku": "FRUITY"},
                ],
            }
        },
        {
            "reference": "2d832fe0-6c96-4515-9be7-4c00983539c5",
            "lineItems": [
                {"sku": "FRUITY", "name": "Fruity", "price": 34.99},
                {"sku": "BANANA-CAKE", "name": "Banana Cake", "price": 17.95},
                {"sku": "BANANA-CAKE", "name": "Banana Cake", "price": 35.9},
                {"sku": "COCOA", "name": "Cocoa", "price": 37.0},
            ],
            "totalPrice": 125.84,
        },
    ),
]


@pytest.mark.parametrize(
    "cart_payload, expected_response", CALCULATE_CART_PRICE_SUCCESSFULLY_DATA
)
def test_calculate_cart_price_successfully(cart_payload, expected_response):
    response = client.post(url="api/cart/calculate-price", json=cart_payload)
    assert response.status_code == 200
    assert response.json() == expected_response
