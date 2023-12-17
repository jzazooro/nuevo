from abc import ABC, abstractmethod

# Interfaz de Estado
class DocumentState(ABC):
    @abstractmethod
    def handle_request(self, document):
        pass

# Estados Concretos
class DraftState(DocumentState):
    def handle_request(self, document):
        print("El documento está en estado de borrador.")
        document.state = ReviewState()

class ReviewState(DocumentState):
    def handle_request(self, document):
        print("El documento está en revisión.")
        document.state = ApprovedState()

class ApprovedState(DocumentState):
    def handle_request(self, document):
        print("El documento ha sido aprobado.")
        document.state = PublishedState()

class PublishedState(DocumentState):
    def handle_request(self, document):
        print("El documento está publicado. No se permiten más cambios.")

# Contexto
class Document:
    def __init__(self):
        self.state = DraftState()

    def change_state(self):
        self.state.handle_request(self)

# Uso del Patrón State
if __name__ == "__main__":
    document = Document()

    # Cambios de estado
    document.change_state()  # De Borrador a Revisión
    document.change_state()  # De Revisión a Aprobado
    document.change_state()  # De Aprobado a Publicado
    document.change_state()  # Intento de cambio en estado Publicado
