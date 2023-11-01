from fileinput import filename
import os
import inquirer
from preguntas import gameInitializationQuestions, construiccionActionQuestions, destruccionQuestions, gameQuestions, importarExportQuestions, getconstruccionesQuestions
from tablero import Tablero
from log import Logger


def main():
    salir = False
    tablero = None
    firstAnswer = inquirer.prompt(gameInitializationQuestions)
    if firstAnswer is not None and firstAnswer['innit'] == 'Comenzar':
        secondAnswer = inquirer.prompt(gameQuestions)
        dinero = float(secondAnswer.get('dinero'))  # type: ignore
        x = int(secondAnswer.get('X'))  # type: ignore
        y = int(secondAnswer.get('Y'))  # type: ignore
        while dinero < 0 or x < 1 or y < 1:
            os.system('cls')
            secondAnswer = inquirer.prompt(gameQuestions)
            dinero = float(secondAnswer.get('dinero'))  # type: ignore
            x = int(secondAnswer.get('X'))  # type: ignore
            y = int(secondAnswer.get('Y'))  # type: ignore
        tablero = Tablero(x, y, dinero)
    elif firstAnswer is not None and firstAnswer['innit'] == 'Importar':
        importar = True
        while importar:
            fileName = inquirer.prompt(importarExportQuestions)
            if fileName is not None:
                tablero = Tablero.importar(fileName['file'])
                if tablero is not None:
                    importar = False
            else:
                Logger.printError("IMPORTAR - Error al importar la partida")
    elif firstAnswer is not None and firstAnswer['innit'] == 'Salir':
        salir = True

    while salir == False:
        if tablero is not None:
            thirdAnswer = inquirer.prompt(
                getconstruccionesQuestions(tablero.getDinero()))
            if thirdAnswer is not None and thirdAnswer['opcion'] == 'Salir':
                salir = True
            elif thirdAnswer is not None and thirdAnswer['opcion'] == 'Construir':
                constructAnswer = inquirer.prompt(construiccionActionQuestions)
                if constructAnswer is not None:
                    tablero.construir(constructAnswer['construccion'], int(
                        constructAnswer['X']), int(constructAnswer['Y']))
                else:
                    Logger.printError(
                        "CONSTRUCCION - Ocurrio un error inesperado")
            elif thirdAnswer is not None and thirdAnswer['opcion'] == 'Destruir':
                destructAnswer = inquirer.prompt(destruccionQuestions)
                if destructAnswer is not None:
                    tablero.destruir(
                        int(destructAnswer['X']), int(destructAnswer['Y']))
                else:
                    Logger.printError(
                        "DESTRUCCION - Ocurrio un error inesperado")
            elif thirdAnswer is not None and thirdAnswer['opcion'] == 'Guardar':
                fileName = inquirer.prompt(importarExportQuestions)
                if fileName is not None and fileName.get('file'):
                    tablero.guardar(fileName.get('file'))  # type: ignore
                else:
                    Logger.printError("GUARDAR - Error al guardar la partida")
        else:
            Logger.printError("TABLERO - El tablero no se pudo inicializar")
            salir = True


main()
