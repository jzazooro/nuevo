from abc import ABC, abstractmethod

# Handler Interface
class ApprovalHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request):
        pass

# Concrete Handlers
class ManagerHandler(ApprovalHandler):
    def handle_request(self, request):
        if request["level"] <= 2:
            print("Aprobado por el Manager")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class DirectorHandler(ApprovalHandler):
    def handle_request(self, request):
        if request["level"] <= 5:
            print("Aprobado por el Director")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class CEOHandler(ApprovalHandler):
    def handle_request(self, request):
        if request["level"] > 5:
            print("Aprobado por el CEO")


manager = ManagerHandler()
director = DirectorHandler()
ceo = CEOHandler()

# Establecer la cadena de responsabilidad
manager.set_next(director).set_next(ceo)

# Crear una solicitud
request = {"level": 4}

# Iniciar el proceso de aprobación
manager.handle_request(request)
