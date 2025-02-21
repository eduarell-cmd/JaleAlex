class Agencia:
    def __init__(self):
        self.carros = []
        self.clientes = []
        self.ventas = []
    
    def add_carro(self,carro):
        self.carros.append(carro)

    def add_cliente(self,cliente):
        self.clientes.append(cliente)
    
    def vender_carro(self,cliente,carro):
        self.ventas.append({"cliente":cliente,"carro":carro})
        self.carros.remove(carro)

    def __str__(self):
        return f"Carros: {self.carros} Clientes: {self.clientes} Ventas: {self.ventas}"
