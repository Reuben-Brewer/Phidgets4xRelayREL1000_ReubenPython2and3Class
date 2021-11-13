# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision C, 11/12/2021

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

from Phidgets4xRelayREL1000_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *

import os, sys, platform
import time, datetime
import threading
import collections

###############
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###############

###############
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
###############

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global Phidgets4xRelayREL1000_ReubenPython2and3ClassObject
    global RELAYS_OPEN_FLAG
    global SHOW_IN_GUI_RELAYS_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if RELAYS_OPEN_FLAG == 1 and SHOW_IN_GUI_RELAYS_FLAG == 1:
                Phidgets4xRelayREL1000_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds

    global Phidgets4xRelayREL1000_ReubenPython2and3ClassObject
    global RELAYS_OPEN_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG

    print("Exiting all threads in test_program_for_MyPrint_ReubenPython2and3Class.")

    EXIT_PROGRAM_FLAG = 1

    #########################################################
    if RELAYS_OPEN_FLAG == 1:
        Phidgets4xRelayREL1000_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

    #########################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global GUI_RootAfterCallbackInterval_Milliseconds

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    TestButton = Button(root, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    #################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_RELAYS_FLAG
    USE_RELAYS_FLAG = 1

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1

    global USE_CycleThroughRelayStatesForTesting_FLAG
    USE_CycleThroughRelayStatesForTesting_FLAG = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_RELAYS_FLAG
    SHOW_IN_GUI_RELAYS_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_RELAYS
    global GUI_COLUMN_RELAYS
    global GUI_PADX_RELAYS
    global GUI_PADY_RELAYS
    global GUI_ROWSPAN_RELAYS
    global GUI_COLUMNSPAN_RELAYS
    GUI_ROW_RELAYS = 1

    GUI_COLUMN_RELAYS = 0
    GUI_PADX_RELAYS = 1
    GUI_PADY_RELAYS = 10
    GUI_ROWSPAN_RELAYS = 1
    GUI_COLUMNSPAN_RELAYS = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 10
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global root

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global Phidgets4xRelayREL1000_ReubenPython2and3ClassObject

    global RELAYS_OPEN_FLAG
    RELAYS_OPEN_FLAG = -1

    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global CycleThroughRelayStatesForTesting_TimeBetweenStateFlips
    CycleThroughRelayStatesForTesting_TimeBetweenStateFlips = 1.0

    global CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread
    CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread = -11111.0

    global CycleThroughRelayStatesForTesting_StateFlipCounter
    CycleThroughRelayStatesForTesting_StateFlipCounter = 0

    global CycleThroughRelayStatesForTesting_RelayStateToBeSet
    CycleThroughRelayStatesForTesting_RelayStateToBeSet = 1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
    #################################################
    #################################################

    #################################################
    #################################################
    global RELAYS_MostRecentDict

    global RELAYS_MostRecentDict_DigitalOutputsList_State
    RELAYS_MostRecentDict_DigitalOutputsList_State = [-1]*4

    global RELAYS_MostRecentDict_DigitalOutputsList_ErrorCallbackFiredFlag
    RELAYS_MostRecentDict_DigitalOutputsList_ErrorCallbackFiredFlag = [-1]*4

    global RELAYS_MostRecentDict_Time
    RELAYS_MostRecentDict_Time = -11111.0

    global Phidgets4xRelayREL1000_ReubenPython2and3ClassObject_GUIparametersDict
    Phidgets4xRelayREL1000_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_RELAYS_FLAG),
                                    ("root", root),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_RELAYS),
                                    ("GUI_COLUMN", GUI_COLUMN_RELAYS),
                                    ("GUI_PADX", GUI_PADX_RELAYS),
                                    ("GUI_PADY", GUI_PADY_RELAYS),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_RELAYS),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_RELAYS)])

    global Phidgets4xRelayREL1000_ReubenPython2and3ClassObject_setup_dict
    Phidgets4xRelayREL1000_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", Phidgets4xRelayREL1000_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                           ("VINT_DesiredSerialNumber", 627656), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                                                           ("VINT_DesiredPortNumber", 5), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                                                           ("DesiredDeviceID", 81),
                                                                           ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                                                                           ("NameToDisplay_UserSet", "Reuben's Test 4xRelay Rel1000_0"),
                                                                           ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                                                           ("MainThread_TimeToSleepEachLoop", 0.002)])

    if USE_RELAYS_FLAG == 1:
        try:
            Phidgets4xRelayREL1000_ReubenPython2and3ClassObject = Phidgets4xRelayREL1000_ReubenPython2and3Class(Phidgets4xRelayREL1000_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            RELAYS_OPEN_FLAG = Phidgets4xRelayREL1000_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("Phidgets4xRelayREL1000_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", root),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_RELAYS_FLAG == 1 and RELAYS_OPEN_FLAG != 1:
        print("Failed to open Phidgets4xRelayREL1000_ReubenPython2and3Class.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_Phidgets4xRelayREL1000_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################

        ###################################################
        if USE_RELAYS_FLAG == 1:

            ##################### SET's
            if USE_CycleThroughRelayStatesForTesting_FLAG == 1:
                if CurrentTime_MainLoopThread - CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread >= CycleThroughRelayStatesForTesting_TimeBetweenStateFlips:
                    Phidgets4xRelayREL1000_ReubenPython2and3ClassObject.SetRelayState(CycleThroughRelayStatesForTesting_StateFlipCounter, CycleThroughRelayStatesForTesting_RelayStateToBeSet)
                    CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread = CurrentTime_MainLoopThread
                    print("CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread: " + str(CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread))

                    if CycleThroughRelayStatesForTesting_StateFlipCounter < 3:
                        CycleThroughRelayStatesForTesting_StateFlipCounter = CycleThroughRelayStatesForTesting_StateFlipCounter + 1
                    else:
                        CycleThroughRelayStatesForTesting_StateFlipCounter = 0
                        if CycleThroughRelayStatesForTesting_RelayStateToBeSet == 0:
                            CycleThroughRelayStatesForTesting_RelayStateToBeSet = 1
                        else:
                            CycleThroughRelayStatesForTesting_RelayStateToBeSet = 0

            #####################

            ##################### GET's
            RELAYS_MostRecentDict = Phidgets4xRelayREL1000_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in RELAYS_MostRecentDict:
                RELAYS_MostRecentDict_DigitalOutputsList_State = RELAYS_MostRecentDict["DigitalOutputsList_State"]
                RELAYS_MostRecentDict_DigitalOutputsList_ErrorCallbackFiredFlag = RELAYS_MostRecentDict["DigitalOutputsList_ErrorCallbackFiredFlag"]
                RELAYS_MostRecentDict_Time = RELAYS_MostRecentDict["Time"]

                #print("RELAYS_MostRecentDict_DigitalOutputsList_State: " + str(RELAYS_MostRecentDict_DigitalOutputsList_State))
            #####################

        ###################################################

        time.sleep(0.002)
    #################################################
    #################################################

    print("Exiting main program 'test_program_for_Phidgets4xRelayREL1000_ReubenPython2and3Class.")
##########################################################################################################
##########################################################################################################