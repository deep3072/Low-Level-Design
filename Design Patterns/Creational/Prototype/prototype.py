import copy
from abc import ABC, abstractmethod

class Document(ABC):
    """
    Prototype interface: Declares a method for cloning itself.
    """
    @abstractmethod
    def clone(self):
        pass

class Resume(Document):
    """
    Concrete prototype 1: Resume which implements the clone method.
    """
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def clone(self):
        return copy.deepcopy(self)
    
    def __repr__(self):
        return f"Resume\n: Name: {self.name}, Experience: {self.experience}\n"

class Report(Document):
    """
    Concrete prototype 2: Report which implements the clone method.
    """
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Report\n: Title: {self.title}, Content: {self.content}\n"
    
class PrototypeRegistry:
    """
    Registry: To store and manage prototypes
    """
    _prototypes = {}
    @staticmethod
    def add_prototype(name, prototype):
        PrototypeRegistry._prototypes[name] = prototype
    
    @staticmethod
    def get_prototype(name):
        return PrototypeRegistry._prototypes.get(name)  
    

# client code
resume_prototype = Resume("Bob", 3)
PrototypeRegistry.add_prototype("bob_resume", resume_prototype)

report_prototype = Report("Design Patterns", "Prototype Pattern")
PrototypeRegistry.add_prototype("design_patterns_report", report_prototype)

resume_clone = PrototypeRegistry.get_prototype("bob_resume").clone()
report_clone = PrototypeRegistry.get_prototype("design_patterns_report").clone()

print("Original Resume:", resume_prototype)
print("Cloned Resume:", resume_clone)

print("Original Report:", report_prototype)
print("Cloned Report:", report_clone)

# Verify deep copy
print("Resume objects are same?:", resume_prototype is resume_clone)
print("Report objects are same?:", report_prototype is report_clone)