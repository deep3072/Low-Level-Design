from abc import ABC, abstractmethod

class IPrint(ABC):
    """
    Interface just for printing
    """
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def get_print_spool_details(self):
        pass
    
class IScan(ABC):
    """
    Interface just for scanning
    """
    @abstractmethod
    def scan(self, document):
        pass
    
    @abstractmethod
    def scan_photo(self):
        pass
    
class IFax(ABC):
    """
    Interface just for faxing
    """
    @abstractmethod
    def fax(self, document):
        pass
    
    @abstractmethod
    def internet_fax(self, document):
        pass
    
class XeroxWorkCentre(IPrint, IScan, IFax):
    """
    This is a Xerox WorkCentre class that functions printing, scanning and faxing.
    """
    def print(self, document):
        print(f"Printing document {document}")
    
    def get_print_spool_details(self):
        print("Getting print spool details")
    
    def scan(self, document):
        print(f"Scanning document {document}")
    
    def scan_photo(self):
        print("Scanning photo")
    
    def fax(self, document):
        print(f"Faxing document {document}")
    
    def internet_fax(self, document):
        print(f"Internet faxing document {document}")

class HPPrinterNScanner(IPrint, IScan):
    """
    This is a HP Printer and Scanner class that functions printing and scanning.
    """
    def print(self, document):
        print(f"Printing document {document}")
    
    def get_print_spool_details(self):
        print("Getting print spool details")
    
    def scan(self, document):
        print(f"Scanning document {document}")
    
    def scan_photo(self):
        print("Scanning photo")

class CanonPrinter(IPrint):
    """
    This is a Canon Printer class that functions only printing.
    """
    def print(self, document):
        print(f"Printing document {document}")
    
    def get_print_spool_details(self):
        print("Getting print spool details")

"""
This design follows ISP helping to segregate the interfaces into smaller and more specific ones making code readibility easier and also applying SRP for ABCs.
"""