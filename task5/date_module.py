from datetime import *


def dateVerification(date: str):
    format = "%d.%m.%Y"
    verif = True

    try:
        verif = bool(datetime.strptime(date, format))
    except ValueError:
        verif = False
    return verif
