class Ingreso:
    def __init__(self):
        self.ingresoList = []

    def regIngreso(self, id, amount):
        ing = (id, amount)
        self.ingresoList.append(ing)

    def impreimirIngreso(self):
        for ing in self.ingresoList:
            print("Id: {ingreso[0]}. Amount: {ingreso[1]}")

    def recuperarIng(self):
        return self.ingresoList
