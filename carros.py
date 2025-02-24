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