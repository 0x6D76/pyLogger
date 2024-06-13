"""
 * File: utilities.py
 * Description: 
 * Functions:
 *           
 * Author: 0x6D76
 * Copyright (c) 2024 0x6D76 (0x6D76@proton.me)
"""
import datetime

PASS = "[PASS]"
FAIL = "[FAIL]"
INFO = "[INFO]"
WARN = "[WARN]"
NONE = ""

EXIT = "Exiting the tool"

# Color Codes
RST = "\x1B[00m"
RED = "\x1B[31m"
GRN = "\x1B[32m"
YEL = "\x1B[33m"
BLU = "\x1B[34m"
MAG = "\x1B[35m"
CYN = "\x1B[36m"

COLOR_MAP = {
    PASS : GRN,
    FAIL : RED,
    INFO : BLU,
    WARN : YEL,
    NONE : RST,
}


def GetCurrentTime () :
    """
    Gets the current time and returns it in the "%D-%M-%Y %H:%M:%S" format
    :return: string holding the formatted timestamp
    """
    currentTime = datetime.datetime.now ()
    return f"{currentTime.strftime ('%d-%m-%y %H:%M:%S')}"
