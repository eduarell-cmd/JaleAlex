#Opcional por si le queremos meter mas chile al queso
class cliente:
    def __init__(self,nombre,apellido,edad,telefono,email,curp):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.curp = curp
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Telefono: {self.telefono} Email: {self.email}"