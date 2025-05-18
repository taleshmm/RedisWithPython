import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()


@pytest.mark.skip(reason="Interaction with database")
def test_insert_product():
   repo = ProductsRepository(conn)
   name = "Test Product"
   price = 10.99
   quantity = 5
   
   repo.insert_product(name, price, quantity)
   assert repo.find_product_by_name(name) is not None
   assert repo.find_product_by_name(name)[1] == name
   assert repo.find_product_by_name(name)[2] == price
   assert repo.find_product_by_name(name)[3] == quantity
   

@pytest.mark.skip(reason="Interaction with database")  
def test_find_product_by_name():
    repo = ProductsRepository(conn)
    name = "Test Product"
    
    product = repo.find_product_by_name(name)
    
    assert product is not None
    assert product[1] == name
    assert product[2] == 10.99
    assert product[3] == 5
