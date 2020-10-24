from ingreso import Ingreso
from salida import Salida

ingreso = Ingreso()
Salida = Salida()


class Finanzas:
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    def fAmount(self):
        ingresoList = Ingreso.recuperarIng()
        salidaList = Salida.recuperarSalida()
        totalIngreso = 0.00
        totalSalida = 0.00

        for ingreso in ingresoList:
            totalIngreso = totalIngreso + ingreso[1]

        for salida in salidaList:
            totalSalida = totalSalida + salida[1]

        amountF = self.amount + totalIngreso - totalSalida

        return amountF

    def regIngreso(self, id, amount):
        ingreso.regIngreso(id, amount)

    def regSalida(self, id, amount):
        Salida.regSalida(id, amount)

    def regTrans(self):
        ingreso.impreimirIngreso()
        Salida.imprimirSalida()

    def recuperarName(self):
        return self.name

    def recuperarId(self):
        return self.id
