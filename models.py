#Opcional por si le queremos meter mas chile al queso
class cliente:
    def __init__(self,nombre,apellido,edad,telefono,email,curp,rfc):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.curp = curp
        self.rfc = rfc
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Telefono: {self.telefono} Email: {self.email}"
class carro:
    def __init__(self,model,branch,year,color,transmition,engine,liters,hp,doors,car_type,precio):
        self.model = model
        self.branch = branch
        self.year = year
        self.color = color
        self.transmition = transmition
        self.engine = engine
        self.liters = liters
        self.hp = hp
        self.doors = doors
        self.car_type = car_type
        self.precio = precio

    def create(self):
        # Code to create a new car record
        pass

    def read(self):
        # Code to read car details
        return {
            "model": self.model,
            "branch": self.branch,
            "year": self.year,
            "color": self.color,
            "transmition": self.transmition,
            "engine": self.engine,
            "liters": self.liters,
            "hp": self.hp,
            "doors": self.doors,
            "car_type": self.car_type
        }

    def update(self, model=None, branch=None, year=None, color=None, transmition=None, engine=None, liters=None, hp=None, doors=None, car_type=None):
        # Code to update car details
        if model is not None:
            self.model = model
        else:
            print("Model is missing")
        if branch is not None:
            self.branch = branch
        else:
            print("Branch is missing")
        if year is not None:
            self.year = year
        else:
            print("Year is missing")
        if color is not None:
            self.color = color
        else:
            print("Color is missing")
        if transmition is not None:
            self.transmition = transmition
        else:
            print("Transmition is missing")
        if engine is not None:
            self.engine = engine
        else:
            print("Engine is missing")
        if liters is not None:
            self.liters = liters
        else:
            print("Liters is missing")
        if hp is not None:
            self.hp = hp
        else:
            print("HP is missing")
        if doors is not None:
            self.doors = doors
        else:
            print("Doors are missing")
        if car_type is not None:
            self.car_type = car_type
        else:
            print("Car type is missing")
        

    def delete(self):
        # Code to delete car record
        del self
class ProcesoVenta:
    def __init__(self, carro):
        self.carro = carro
        self.cliente = cliente

    def validar_costo(self,carro):
        precio_carro = carro.precio
        opciones_financiamiento = {
            12: 0.05,  
            24: 0.10,  
            32: 0.15   
        }

        
        enganche = float(input("Ingrese el porcentaje de enganche (entre 20 y 50): "))
        if enganche < precio_carro*(0.2) or enganche > precio_carro*(0.5):
             raise ValueError("El porcentaje de enganche debe estar entre 20 y 50")

        tabla_financiamiento = []

        for meses, interes in opciones_financiamiento.items():
            monto_financiado = precio_carro - enganche
            monto_total_con_interes = monto_financiado * (1 + interes)
            mensualidad = monto_total_con_interes / meses
            tabla_financiamiento.append({
            'meses': meses,
            'enganche': enganche,
            'mensualidad': mensualidad,
            'interes': interes,
            'monto_total_con_interes': monto_total_con_interes
            })

        return tabla_financiamiento

class Agencia:
    def __init__(self):
        self.carros = []
        self.clientes = {}
        self.ventas = []
    
    def inventario(self,arr):
        for auto in arr:
            car = carro(auto["modelo"],auto["marca"],auto["año"],auto["color"],auto["transmision"],auto["motor"],auto["litros"],auto["hp"],auto["puertas"],auto["tipo_de_carro"],auto["precio"])
            self.add_carro(car)

    def add_carro(self,carro):
        self.carros.append(carro)

    def add_cliente(self,cliente):
        self.clientes.append(cliente)
    
    def vender_carro(self,cliente,carro):
        self.ventas.append({"cliente":cliente,"carro":carro})
        self.carros.remove(carro)
        #conectar con la base de datos y guardar la venta, remover el csrro de inventario

    def __str__(self):
        return f"Carros: {self.carros} Clientes: {self.clientes} Ventas: {self.ventas}"


