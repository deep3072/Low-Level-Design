class ProductCatalog: # High-level module
    def list_all_products(self):
        sql_product_repository = SQLProductRepository() # directly dependent on SQLProductRepository
        sql_product_repository.get_all_product_names()

class SQLProductRepository: # Low-level module
    def get_all_product_names(self):
        all_products = ["Product 1", "Product 2", "Product 3"] # logic to get all products
        return all_products
    
"""
Here, high-level module is directly dependent on low-level module which violtes Dependency Inversion Principle.
"""
    