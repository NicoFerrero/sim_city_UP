import inquirer

gameInitializationQuestions = [
    inquirer.List('innit',
                  message='Bienvenido al Juego!!',
                  choices=['Comenzar', 'Importar', 'Salir']
                  ),
]

gameQuestions = [
    inquirer.Text('dinero', message='Con cuanto dinero desea comenzar?'),
    inquirer.Text('X', message='Cuanto quiere que sea el ancho del tablero?'),
    inquirer.Text('Y', message='Cuanto quiere que sea el alto del tablero?')
]


def getconstruccionesQuestions(dinero: float):
    return [inquirer.List('opcion',
                          message='Que accion desea hacer? Su dinero actual es $ ' +
                          str(dinero),
                          choices=["Construir", "Destruir",
                                   "Guardar", "Salir"],
                          )]


construiccionActionQuestions = [
    inquirer.List('construccion',
                  message='Que desea construir?',
                  choices=["Calle", "ZonaA", "ZonaB", "ZonaC"]
                  ),
    inquirer.Text('X', message='Inserte posicion X para la construccion'),
    inquirer.Text('Y', message='Inserte posicion Y para la construccion')
]

destruccionQuestions = [
    inquirer.Text('X', message='Inserte posicion X para la destruccion'),
    inquirer.Text('Y', message='Inserte posicion Y para la destruccion')
]

importarExportQuestions = [
    inquirer.Text(
        'file', message='Ingrese el nombre de la partida con el .json al final'),
]
