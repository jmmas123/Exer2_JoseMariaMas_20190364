class Salida:
    def __int__(self):
        self.salidaList = []

    def regSalida(self, id, amount):
        salida = (id, amount)
        self.salidaList.append(salida)

    def imprimirSalida(self):
        for salida in self.salidaList:
            print("Id: {salida[0]}. Amount: {salida[1]}")

    def recuperarSalida(self):
        return self.salidaList
