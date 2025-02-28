from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def is_loyal_customer(self):
        raise NotImplementedError("Subclass must implement abstract method")

class HealthInsuranceCustomer(Customer):
    def __init__(self, is_loyal: bool):
        self.is_loyal = is_loyal
        
    def is_loyal_customer(self):
        return self.is_loyal

class CarInsuranceCustomer(Customer):
    def __init__(self, is_loyal: bool):
        self.is_loyal = is_loyal
        
    def is_loyal_customer(self):
        return self.is_loyal
    
class InsurancePremiumDiscountCalculator:
    def calculate_premium_discount_percentage(self, customer: Customer):
        if customer.is_loyal_customer():
            return 20
        else:
            return 0
        
"""
Now this follows ocp because if we want to add new insurance type like HomeInusranceCustomer, we can do so by creating a new class and implementing the CustomerProfile interface. We do not need to modify InsurancePremiumDiscountCalculator.
"""