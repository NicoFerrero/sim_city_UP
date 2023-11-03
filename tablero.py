import json
from construccion import Construccion, Calle, ZonaA, ZonaB, ZonaC
from log import Logger


class Celda:
    def __init__(self, posX, posY):
        self.__posX = posX
        self.__posY = posY
        self.__construccion = None

    def getConstruccion(self):
        return self.__construccion

    def setConstruccion(self, construccion):
        self.__construccion = construccion


class Tablero:
    def __init__(self, x: int, y: int, dinero: float, tablero=None):
        self.__x = x
        self.__y = y
        self.__dinero = dinero
        if tablero is None:
            self.__tablero = self.__crearTablero(x, y)
        else:
            self.__tablero = self.__crearTableroImportado(tablero)
        self.__mostrarTablero()

    def getDinero(self):
        return self.__dinero

    def __crearTablero(self, x: int, y: int):
        arr = []
        for i in range(y):
            row = []
            for j in range(x):
                row.append(Celda(i, j))
            arr.append(row)
        return arr

    def __crearTableroImportado(self, tablero):
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                celda = tablero[i][j].get('_Celda__construccion')
                if celda is None:
                    tablero[i][j] = Celda(i, j)
                elif celda.get('_Construccion__precio') == 5:
                    celdaConstruct = Celda(i, j)
                    celdaConstruct.setConstruccion(Calle())
                    tablero[i][j] = celdaConstruct
                elif celda.get('_Construccion__precio') == 10:
                    celdaConstruct = Celda(i, j)
                    celdaConstruct.setConstruccion(ZonaA())
                    tablero[i][j] = celdaConstruct
                elif celda.get('_Construccion__precio') == 20:
                    celdaConstruct = Celda(i, j)
                    celdaConstruct.setConstruccion(ZonaB())
                    tablero[i][j] = celdaConstruct
                elif celda.get('_Construccion__precio') == 30:
                    celdaConstruct = Celda(i, j)
                    celdaConstruct.setConstruccion(ZonaC())
                    tablero[i][j] = celdaConstruct
        return tablero

    def __mostrarTablero(self):
        board = ''
        for i in range(len(self.__tablero)):
            for j in range(len(self.__tablero[i])):
                if self.__tablero[i][j].getConstruccion() is None:
                    board += '\t[] '
                elif isinstance(self.__tablero[i][j].getConstruccion(), Calle):
                    board += '\tC '
                elif isinstance(self.__tablero[i][j].getConstruccion(), ZonaA):
                    board += '\t* '
                elif isinstance(self.__tablero[i][j].getConstruccion(), ZonaB):
                    board += '\t** '
                elif isinstance(self.__tablero[i][j].getConstruccion(), ZonaC):
                    board += '\t*** '
            board += '\n'
        print(board)

    def construir(self, construccionArg: str, x: int, y: int):
        pudoConstruir = False
        construccion = Construccion.parseConstruccion(construccionArg)
        try:
            if construccion is not None and self.__tablero[x][y].getConstruccion() is None:
                if self.__dinero - construccion.getPrecio() < 0:
                    Logger.printWarning(
                        "No tiene dinero suficiente para construir!!")
                else:
                    self.__dinero -= construccion.getPrecio()
                    self.__tablero[x][y].setConstruccion(construccion)
                    pudoConstruir = True
                    Logger.printSuccess("Le quedan $" + str(self.__dinero))
            else:
                Logger.printWarning("Ya hay una construccion en esta casilla")
        except IndexError:
            Logger.printError(
                f'La posicion [{x}][{y}] esta fuera del rango del tablero. El tablero va de [0][0] a [{self.__y-1}][{self.__x-1}]')
        self.__mostrarTablero()
        return pudoConstruir

    def destruir(self, x: int, y: int):
        pudoDestruir = False
        if self.__tablero[x][y].getConstruccion() is not None:
            if self.__dinero - self.__tablero[x][y].getConstruccion().getPrecio() / 2 < 0:
                Logger.printWarning(
                    "No tiene dinero suficiente para destruir!!")
            else:
                self.__dinero -= self.__tablero[x][y].getConstruccion(
                ).getPrecio() / 2
                self.__tablero[x][y].setConstruccion(None)
                pudoDestruir = True
                Logger.printSuccess("Le quedan $" + str(self.__dinero))
        else:
            Logger.printWarning("No hay una construccion en esta casilla")
        self.__mostrarTablero()
        return pudoDestruir

    def guardar(self, fileName: str):
        jsonObject = json.dumps(self, cls=CarJSONEncoder)
        with open(fileName, 'w') as outfile:
            outfile.write(jsonObject)

    @staticmethod
    def importar(fileName: str):
        try:
            with open(fileName, "r") as openfile:
                json_object = json.load(openfile)
                tablero = Tablero(json_object.get('_Tablero__x'), json_object.get(
                    '_Tablero__y'), json_object.get('_Tablero__dinero'), json_object.get('_Tablero__tablero'))
                return tablero
        except FileNotFoundError:
            Logger.printError(
                'IMPORTAR- No se encontro un archivo con ese nombre')


class CarJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
