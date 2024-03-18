import pytest

from src.products.domain.value_objects import ProductId
from src.products.domain.errors import ProductError

def test_can_create_product_from_valid_nanoid():
    #given
    product_id = ProductId.of('N45MPgAPw0')

    #then
    assert isinstance(product_id, ProductId)
    assert product_id.get() is 'N45MPgAPw0'

def test_should_raise_product_error_if_invalid_nanoid():
    # expect
    with pytest.raises(ProductError):
        ProductId.of("123")

def test_can_create_new_product_id() -> None:
    # expect
    assert isinstance(ProductId.new(), ProductId)


def test_product_id_eq() -> None:
    # expect
    assert ProductId.of('N45MPgAPw0') == ProductId.of('N45MPgAPw0')