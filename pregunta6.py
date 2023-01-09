class mochila:
    def __innit__(self,pesomaximo:int,peso:list[int],precios:list[int]):
        self.pesomaximo=pesomaximo
        self.peso=peso
        self.precios=precios
        pesomaximo=100
        peso=[12,23,11,15,7]
        precios=[103,60,70,5,15]
    def problema(self):
        contador =+ 0
        if contador==0 or self.pesomaximo==0:
            return 0
        if self.peso[contador-1] < self.pesomaximo:
            return max(self.pesomaximo,self.peso,self.precios,contador -1)
        else:
            return 'Los pesos exceden el peso maximo'
        


