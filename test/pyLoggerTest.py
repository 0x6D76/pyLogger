"""
 * File: pyLoggertest.py
 * Description: The file contains unit test cases as part of testing pyLogger
 * Functions:
 *           def SetupModule ()
 *           def testLoggerInit ()
 *           def testLoggerHeader ()
 *           def testLoggerLog ()
 *           def testGetCurrentTime ()
 *           def testColorMap ()
 *           def testLoggerFooter ()
 *           def testInitializeDir ()
 *
 * Author: 0x6D76
 * Copyright (c) 2024 0x6D76 (0x6D76@proton.me)
"""
import os
from pyLogger.logger import Logger
from pyLogger.utilities import (GetCurrentTime, InitializeDir, COLOR_MAP,
                                PASS, FAIL, INFO, WARN, GRN, RED, BLU, YEL)

# Test data
LOG_FILE = "test_log.log"
TOOL = "testTool"
VER = "1.0"
TAG = "test"
DIRS = ["Logs", "Logs/Inside", "Hello"]


# Cleanup any existing log file
def SetupModule ():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    for d in DIRS:
        if os.path.exists (d):
            os.remove (d)


# Test Logger initialization
def testLoggerInit():
    logger = Logger(logFile=LOG_FILE, verbose=True)
    assert logger.logFile == LOG_FILE
    assert logger.verbose is True


# Test Header method
def testLoggerHeader():
    logger = Logger(logFile=LOG_FILE, verbose=True)
    logger.Header ("tester")
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
    assert "=" * 80 in lines[0]  # Check if header is written to the log file
    assert "tester" in lines [1]


# test Log method
def testLoggerLog():
    logger = Logger(logFile=LOG_FILE, verbose=True)
    logger.Log(severity=PASS, module="test_module", rCode = 1, user = True, optional = "testing log message.")
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
    assert any("testing log message." in line for line in lines)  # Check if log message is written to the log file


# Test GetCurrentTime function
def testGetCurrentTime():
    current_time = GetCurrentTime()
    assert current_time is not None


# Test COLOR_MAP dictionary
def testColorMap():
    assert COLOR_MAP[PASS] == GRN
    assert COLOR_MAP[FAIL] == RED
    assert COLOR_MAP[INFO] == BLU
    assert COLOR_MAP[WARN] == YEL


# Test Footer function
def testLoggerFooter():
    logger = Logger(logFile=LOG_FILE, verbose=True)
    logger.Footer()
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
    assert "=" * 80 in lines[-1]  # Check if footer is written to the log file


# Test InitializeDir function
def testInitializeDir ():
    InitializeDir (DIRS)
    for d in DIRS:
        assert os.path.exists (d)
