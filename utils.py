class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ERROR = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

no_errors = False
silent = False

def setNoErrors(boolean):
    global no_errors
    no_errors = boolean

def setSilent(boolean):
    global silent
    silent = boolean

def showCriticalError(text: str):
    print(f"{Colors.FAIL}[ CRITICAL ERROR ]{Colors.ENDC} {text}")

def showError(text: str):
    if not no_errors:
        print(f"{Colors.ERROR}[ ERROR ]{Colors.ENDC} {text}")

def showSuccess(text: str):
    if not silent:
        print(f"{Colors.OKGREEN}[ SUCCESS ]{Colors.ENDC} {text}")

def showInfo(text: str):
    if not silent:
        print(f"{Colors.OKBLUE}[ INFO ]{Colors.ENDC} {text}")

def showWarning(text: str):
    if not no_errors:
        print(f"{Colors.WARNING}[ WARNING ]{Colors.ENDC} {text}")
