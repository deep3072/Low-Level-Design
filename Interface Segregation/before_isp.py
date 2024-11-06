from abc import ABC, abstractmethod

class IMultiFunctionDevice(ABC):
    """
    This is a multi function device interface that has 5 functions.
    """
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def get_print_spool_details(self):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass
    
    @abstractmethod
    def scan_photo(self):
        pass
    
    @abstractmethod
    def fax(self, document):
        pass
    
    @abstractmethod
    def internet_fax(self, document):
        pass

class XeroxWorkCentre(IMultiFunctionDevice):
    """
    This is a Xerox WorkCentre class that implements the IMultiFunctionDevice .
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

class HPPrinterNScanner(IMultiFunctionDevice):
    """
    This is a HP Printer and Scanner class that implements the IMultiFunctionDevice but it only does printing and scanning so it keeps rest of the methods blank.
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
        pass
    
    def internet_fax(self, document):
        pass
    
class CanonPrinter(IMultiFunctionDevice):
    """
    This is a Canon Printer class that implements the IMultiFunctionDevice but it only does printing so it keeps rest of the methods blank.
    """
    def print(self, document):
        print(f"Printing document {document}")
    
    def get_print_spool_details(self):
        print("Getting print spool details")
    
    def scan(self, document):
        pass
    
    def scan_photo(self):
        pass
    
    def fax(self, document):
        pass
    
    def internet_fax(self, document):
        pass
    
"""
Now this fat interface, blank methods are bad design and it does not follow ISP. 
"""