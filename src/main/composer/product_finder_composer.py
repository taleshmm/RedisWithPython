from src.main.server.server_settings import redis_connection_handler, sqlite_connection_handler
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.products_repository import ProductsRepository
from src.data.product_finder import ProductFinder


def product_finder_composer():
    redis_conn = redis_connection_handler.get_connection()
    sqlite_conn = sqlite_connection_handler.get_connection()
    
    redis_repository = RedisRepository(redis_conn)
    products_repository = ProductsRepository(sqlite_conn)
    
    return ProductFinder(redis_repository, products_repository)
    
    
    