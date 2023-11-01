class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def printError(texto: str):
        print(Logger.FAIL + texto + Logger.ENDC)

    @staticmethod
    def printSuccess(texto: str):
        print(Logger.OKGREEN + texto + Logger.ENDC)

    @staticmethod
    def printWarning(texto: str):
        print(Logger.WARNING + texto + Logger.ENDC)
