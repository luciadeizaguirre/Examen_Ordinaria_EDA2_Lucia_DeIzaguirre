class Artefacto:
    def __init__(self,nombre,peso,precio,fechacad):
        self.peso=peso
        self.nombre=nombre
        self.precio=precio
        self.fechacad=fechacad
        print ("Se ha creado con exito el artefacto")
    def __str__(self):
        return f'Se ha creado el artefacto {self.nombre}, con peso {self.peso}, que cuesta {self.precio} euros y caduca el {self.fechacad}'
