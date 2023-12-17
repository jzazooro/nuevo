from abc import ABC, abstractmethod
import datetime

# Interfaz común para el Documento Real y el Proxy
class DocumentInterface(ABC):
    @abstractmethod
    def display_content(self):
        pass

# Documento Real
class Document(DocumentInterface):
    def __init__(self, content):
        self.content = content

    def display_content(self):
        print(f"Contenido del Documento: {self.content}")

# Proxy de Documento
class DocumentProxy(DocumentInterface):
    def __init__(self, document: Document):
        self.document = document

    def display_content(self):
        # Aquí se pueden agregar controles de seguridad y registro
        self.log_access()
        self.check_access_rights()
        self.document.display_content()

    def log_access(self):
        # Registro de acceso
        print(f"Acceso al documento registrado en {datetime.datetime.now()}")

    def check_access_rights(self):
        # Aquí se pueden implementar controles de seguridad
        # Por ejemplo: verificar permisos del usuario, autenticación, etc.
        print("Verificación de permisos realizada")

# Uso del Proxy
real_document = Document("Información confidencial")
proxy_document = DocumentProxy(real_document)

# El cliente interactúa con el Proxy
proxy_document.display_content()
