class carro:
    def __init__(self,model,branch,year,color,transmition,engine,liters,hp,doors,car_type):
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

    def __str__(self):
        return f"Model: {self.model} Branch: {self.branch} Year: {self.year} Color: {self.color} Transmition: {self.transmition} Engine: {self.engine} Liters: {self.liters} HP: {self.hp} Doors: {self.doors} Car Type: {self.car_type}"
    
    
    