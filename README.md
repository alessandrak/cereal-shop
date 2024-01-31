# Cereal Shop API

This FastAPI project addresses the challenge of implementing an API for calculating a shopping cart's total at a Cereal Shop.

## Running locally

Ensure you have Python 3.10+ and pip installed. Activate your Python environment before executing the following commands:

Install the dependecies: 
```bash
make install
```

Setup data and run:
```bash
make run
```

Run tests:
```bash
make test
```

## Running with Docker

Build and run docker image:
```bash
make docker-up
```

To run tests in a separate terminal (ensure the container is active):

```bash
make docker-test
```

## API Usage
Access the API documentation at `/docs`. Use the following command to test the cart price calculation:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "cart": {
    "reference": "2d832fe0-6c96-4515-9be7-4c00983539c1",
    "lineItems": [
      { "name": "Peanut Butter", "price": "39.0", "sku": "PEANUT-BUTTER" },
      { "name": "Fruity", "price": "34.99", "sku": "FRUITY" },
      { "name": "Chocolate", "price": "32", "sku": "CHOCOLATE" }
    ]
  }
}' http://0.0.0.0:8000/api/cart/calculate-price
```

## Considerations

The execution commands are already linked to the database setup, configuring the following data:
```json
{
  "prerequisite_skus": ["PEANUT-BUTTER", "COCOA", "FRUITY"],
  "eligible_skus": ["BANANA-CAKE", "COCOA", "CHOCOLATE"],
  "discount_unit": "percentage",
  "discount_value": "50.0"
} 
```