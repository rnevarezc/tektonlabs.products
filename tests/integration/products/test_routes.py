import pytest
from fastapi import status
from fastapi.testclient import TestClient
from kink import di

from src.products.application.services import ProductService
from src.products.domain.repositories import ProductRepository
from src.products.domain.entities import Product
from src.main import app

client = TestClient(app)

product_test_body = {
    "Name": "Macbook",
    "Description": "A Laptop",
    "Status": "1",
    "Stock": "5",
    "Price": 1299.99
}

@pytest.mark.usefixtures("setup_di")
def test_create_product():
    # with
    body = product_test_body

    # when
    response = client.post("/products/", json=body)

    # then
    assert response.status_code == status.HTTP_201_CREATED
    payload = response.json()
    assert "ProductId" in payload
    assert payload["Name"] == body["Name"]
    assert payload["Description"] == body["Description"]
    assert payload["StatusName"] == "Active"
    assert payload["Price"] == body["Price"]
    assert "CreatedAt" in payload


@pytest.mark.usefixtures("setup_di")
@pytest.mark.asyncio
async def test_get_product(product_repository: ProductRepository):
    # with
    product = Product.create(**product_test_body)
    await product_repository.create(product)
    
    # when
    response = client.get(f"/products/{product.ProductId}")

    # then
    # to-do: Check if I can validate the ProductDTO structure directly
    assert response.status_code == status.HTTP_200_OK
    payload = response.json()    
    assert payload["ProductId"] == product.ProductId.get()
    assert payload["Name"] == product.Name
    assert payload["Description"] == product.Description
    assert payload["StatusName"] == "Active"
    assert payload["Stock"] == product.Stock
    assert payload["Price"] == product.Price.get()
    assert "Discount" in payload
    assert "FinalPrice" in payload
    assert "CreatedAt" in payload


@pytest.mark.usefixtures("setup_di")
@pytest.mark.asyncio
async def test_update_product(product_repository: ProductRepository):
    
    # with
    product = Product.create(**product_test_body)
    await product_repository.create(product)

    # when
    product_update_body = {
        "Name": "Macbook Air",
        "Description": "An Apple Laptop",
        "Status": 0,
        "Stock": 10,
        "Price": 999.99
    }
    response = client.put(f"/products/{product.ProductId}", json=product_update_body)

    #then
    assert response.status_code == status.HTTP_200_OK
    payload = response.json()    
    assert payload["ProductId"] == product.ProductId.get()
    assert payload["Name"] == product_update_body["Name"]
    assert payload["Description"] == product_update_body["Description"]
    assert payload["StatusName"] == "Inactive"
    assert payload["Stock"] == product_update_body["Stock"]
    assert payload["Price"] == product_update_body["Price"]