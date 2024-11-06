class Employee:
    def __init__(self, employeeId, employeeName, employeeAddress, contactNumber, employeeType):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.employeeAddress = employeeAddress
        self.contactNumber = contactNumber
        self.employeeType = employeeType
    
    def save(self):
        # Save employee to database
        print(f"Saving Employee {self.employeeName} to database with details {self.employeeId}, {self.employeeAddress}, {self.contactNumber}, {self.employeeType}")
        pass
    
    def calculate_tax(self):
        if self.employeeType == "fulltime":
            # Calculate tax for fulltime employee logic
            print("Calculating tax for fulltime employee")
        elif self.employeeType == "parttime":
            # Calculate tax for parttime employee
            print("Calculating tax for parttime employee")

# Reasons to change for this class:
"""
1. Changes in emp details
2. Changes in db column names or db schema
3. changes in tax calculation logic
"""