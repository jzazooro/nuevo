from prueba import *
from prueba2 import *
from prueba3 import *
from prueba4 import *



def navigate(folder):
    """ Navegar por una carpeta y mostrar su contenido. """
    folder.show_details()

def create_document(folder, document_name):
    """ Crear un nuevo documento en una carpeta. """
    new_document = Document(document_name)
    folder.add(new_document)

def modify_document(document, new_content):
    """ Modificar el contenido de un documento. """
    document.content = new_content

def delete_document(folder, document):
    """ Eliminar un documento de una carpeta. """
    folder.remove(document)

def request_access(document_proxy):
    """ Solicitar acceso a un documento a través de su proxy. """
    document_proxy.display_content()

def change_document_state(document):
    """ Cambiar el estado de un documento. """
    document.change_state()

modify_document(doc1, "Nuevo contenido para Doc1")

# Solicitar acceso y mostrar contenido (usando Proxy)
doc_proxy = DocumentProxy(doc1)
request_access(doc_proxy)

# Cambiar el estado de un documento (usando State)
change_document_state(doc1)

modify_document(doc1, "Nuevo contenido para Doc1")



# Solicitar acceso y mostrar contenido (usando Proxy)
doc_proxy = DocumentProxy(doc1)
request_access(doc_proxy)

# Cambiar el estado de un documento (usando State)
change_document_state(doc1)
