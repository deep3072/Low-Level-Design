from abc import ABC, abstractmethod

class ProductRepository(ABC):
    """
    An abstraction between the high-level module and the low-level module.
    """
    @abstractmethod
    def get_all_product_names(self):
        pass
    
class SQLProductRepository(ProductRepository): # Low-level module
    """
    Low-level module that implements the abstraction.
    """
    def get_all_product_names(self):
        all_products = ["Product 1", "Product 2", "Product 3"] # logic to get all products
        return all_products
    
class ProductFactory:
    """
    Factory class to keep the high-level module and low-level module loosely coupled.
    """
    def create(self):
        return SQLProductRepository()

class ProductCatalog: # High-level module
    def list_all_products(self):
        product_repository = ProductFactory().create() # invoke the factory method and get the object, instead of depending on the concrete class
        product_repository.get_all_product_names()
        
"""
Here, an abstraction is added to separate the high-level module from the low-level module. The high-level module uses Factory class to get the object of the low-level module so that it becomes loosely coupled.
"""