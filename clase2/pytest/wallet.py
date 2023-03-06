

class Insuficientesaldo(Exception):
    pass

class wallet():
    
    def __init__(self, cantidad=0):
        self.saldo = cantidad
    
    def gastar_dinero(self, cantidad):
        if self.saldo < cantidad:
            raise Insuficientesaldo ("No hay suficiente saldo en tu cuenta")
        else:
            self.saldo -= cantidad
            
    def anadir_saldo(self, cantidad):
        self.saldo += cantidad
