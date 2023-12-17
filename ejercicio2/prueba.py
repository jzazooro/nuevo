from abc import ABC, abstractmethod
from typing import List

# Componente abstracto
class FileSystemEntity(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Hoja: Documento
class Document(FileSystemEntity):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Documento: {self.name}")

# Hoja: Enlace
class Link(FileSystemEntity):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def show_details(self):
        print(f"Enlace: {self.name}, URL: {self.url}")

# Compuesto: Carpeta
class Folder(FileSystemEntity):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemEntity):
        self.children.append(component)

    def remove(self, component: FileSystemEntity):
        self.children.remove(component)

    def show_details(self):
        print(f"Carpeta: {self.name}")
        for child in self.children:
            child.show_details()

# Uso del patrón Composite
root = Folder("Raíz")
folder1 = Folder("Carpeta 1")
folder2 = Folder("Carpeta 2")

doc1 = Document("Documento1.txt")
doc2 = Document("Documento2.pdf")
link1 = Link("Enlace1", "http://example.com")

folder1.add(doc1)
folder2.add(doc2)
folder2.add(link1)

root.add(folder1)
root.add(folder2)

# Muestra la estructura
root.show_details()
