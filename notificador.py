class Observable:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.notify(message)

class Observer:
    def notify(self, message):
        raise NotImplementedError("Debes implementar este método")

class Cliente(Observer):
    def __init__(self, nombre):
        self.nombre = nombre

    def notify(self, message):
        print(f"{self.nombre}, hay una nueva promoción: {message}")

class SistemaPromociones(Observable):
    def agregar_promocion(self, promocion):
        self.notify_observers(promocion)

# Ejemplo de uso
sistema_promociones = SistemaPromociones()

cliente1 = Cliente("Juan")

sistema_promociones.subscribe(cliente1)

sistema_promociones.agregar_promocion("30% de descuento en tu próxima compra")
