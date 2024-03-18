from src.products.domain.entities import Product
from src.products.domain.value_objects import ProductId

def test_can_update_discount():
    #given
    product = Product.create(
        Name="Macbook",
        Description="A laptop",
        Status=1,
        Stock=10,
        Price=20
    )

    #when
    product.update_discount(10)

    #then
    assert isinstance(product.ProductId, ProductId)
    assert product.Discount.get() == 10
    assert product.FinalPrice.get() == 18

def test_can_update():
    #given
    product = Product.create(
        Name="Macbook",
        Description="A laptop",
        Status=1,
        Stock=10,
        Price=20
    )
    assert product.UpdatedAt is None

    #when
    product.update(**{"Name": "Macbook Air", "Status": 0, "Stock": 5, "Price": 30})

    #then
    assert product.Name is "Macbook Air"
    assert product.UpdatedAt is not None