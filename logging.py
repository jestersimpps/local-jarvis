from colorama import init, Fore, Style
from kink import inject


@inject
class Logging:

    def __init__(self):
        init(autoreset=True)

    def logInfo(self, message: str):
        print(Fore.LIGHTYELLOW_EX + message + Style.RESET_ALL)

    def logError(self, message: str):
        print(Fore.LIGHTRED_EX + message + Style.RESET_ALL)

    def logUser(self, message: str):
        print(Fore.CYAN + message + Style.RESET_ALL)

    def logLlm(self, message: str):
        print(Fore.GREEN + message + Style.RESET_ALL, end="", flush=True)
