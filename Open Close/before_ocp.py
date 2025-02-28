class HealthInsuranceCustomer:
    def __init__(self, is_loyal: bool):
        self.is_loyal = is_loyal
        
    def is_loyal_customer(self):
        return self.is_loyal

class CarInsuranceCustomer:
    def __init__(self, is_loyal: bool):
        self.is_loyal = is_loyal
        
    def is_loyal_customer(self):
        return self.is_loyal
    
class InsurancePremiumDiscountCalculator:
    def calculate_premium_discount_percentage_health(self, customer: HealthInsuranceCustomer):
        if customer.is_loyal_customer():
            return 20
        else:
            return 0
    def calculate_premium_discount_percentage_car(self, customer: CarInsuranceCustomer):
        if customer.is_loyal_customer():
            return 20
        else:
            return 0



"""
Situation: Make InsurancePremiumDiscountCalculator open for extension and closed for modification
but currently is only supports health insurance customers and does not support for car insurance customers, assuming ducktyping will raise some error for car insurance customers.
"""        