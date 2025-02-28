class Employee:
    def __init__(self, employeeId, employeeName, employeeAddress, contactNumber, employeeType):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.employeeAddress = employeeAddress
        self.contactNumber = contactNumber
        self.employeeType = employeeType
        
class TaxCalculator:
    def calculate_tax(self, employeeType):
        # logic for calculating tax based on parttime or fulltime employee
        print("Calculating tax for parttime or fulltime employee")

class EmployeeRepository:
    def save(self, employee):
        # Save employee to database
        print(f"Saving Employee {employee.employeeName} to database with details {employee.employeeId}, {employee.employeeAddress}, {employee.contactNumber}, {employee.employeeType}")
        pass
    
class EmployeeService:
    def __init__(self):
        self.employeeRepository = EmployeeRepository()
        self.taxCalculator = TaxCalculator()
    
    def save_employee_details(self, employee):
        self.employeeRepository.save(employee)
        
    def calculate_tax(self, employee):
        self.taxCalculator.calculate_tax(employee.employeeType)
        
"""
Every class has their defined responsibility now.
"""