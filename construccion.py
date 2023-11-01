class Construccion:
    def __init__(self, precio):
        self.__precio = precio

    def getPrecio(self) -> int:
        return self.__precio

    @staticmethod
    def parseConstruccion(construccionStr: str):
        construccion = None
        if construccionStr == 'Calle':
            construccion = Calle()
        elif construccionStr == 'ZonaA':
            construccion = ZonaA()
        elif construccionStr == 'ZonaB':
            construccion = ZonaB()
        elif construccionStr == 'ZonaC':
            construccion = ZonaC()
        return construccion

class Calle(Construccion):
    def __init__(self):
        super().__init__(5)

class ZonaA(Construccion):
    def __init__(self):
        super().__init__(10)

class ZonaB(Construccion):
    def __init__(self):
        super().__init__(20)

class ZonaC(Construccion):
    def __init__(self):
        super().__init__(30)