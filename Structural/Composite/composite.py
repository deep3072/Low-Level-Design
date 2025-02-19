from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    """
    Component: interface for all common operations of leaf and composite
    """
    @abstractmethod
    def display(self, indent=0):
        pass

class File(FileSystemComponent):
    """
    Leaf (Concrete component 1): represents a file in the File system
    """
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}")

class Directory(FileSystemComponent):
    """
    Composite (Concrete component 2): represents a directory in the File system
    """
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)

file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

root_dir = Directory("root")
sub_dir1 = Directory("sub_dir1")
sub_sub_dir1 = Directory("sub_sub_dir1")

root_dir.add(file1)
root_dir.add(sub_dir1)
root_dir.add(file2)
sub_dir1.add(sub_sub_dir1)
sub_dir1.add(file3)


sub_dir1.display() # Display the sub-directory
print("\n\n")
root_dir.display() # Display the entire file system