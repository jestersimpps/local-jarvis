from colorama import init, Fore, Style


class Logging:

    def __init__(self):
        init(autoreset=True)

    def logInfo(message: str):
        print(Fore.LIGHTYELLOW_EX + message + Style.RESET_ALL)

    def logError(message: str):
        print(Fore.LIGHTRED_EX + message + Style.RESET_ALL)
        
    def logUser(message: str):
        print(Fore.LIGHTCYAN_EX + message + Style.RESET_ALL)
        
    def logLlm(message: str):
        print(Fore.LIGHTBLUE_EX + message + Style.RESET_ALL)
