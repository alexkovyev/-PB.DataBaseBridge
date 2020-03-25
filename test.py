from DBBridge.DbCon.dbconfig import dbconfig
from DBBridge.dbbridge import db_bridge, BridgeError
import threading

def thred_1():
    try:
        bridge = db_bridge()
        print(bridge.execute('FN_GetAllStffsInSystem', [None]))
    except BridgeError:
        print ("AHTUNG!")

def thred_2():
    try:
        bridge = db_bridge()
        print(bridge.execute('FN_GetAllStffsInSystem', [None]))
    except BridgeError as error:
        print ("AHTUNG 2!", error)

def thred_3():
    try:
        bridge = db_bridge()
        print(bridge.execute('FN_GetAllStffsInSystem', [None]))
    except BridgeError as error:
        print ("AHTUNG 3!", error)

def thred_4():
    try:
        bridge = db_bridge()
        print(bridge.execute('FN_GetAllStffsInSystem', [None]))
    except BridgeError as error:
        print ("AHTUNG 4!", error)

def thred_5():
    try:
        bridge = db_bridge()
        print(bridge.execute('FN_GetAllStffsInSystem', [None]))
    except BridgeError as error:
        print ("AHTUNG 5!", error)


one = threading.Thread(target=thred_1)
two = threading.Thread(target=thred_2)
three = threading.Thread(target=thred_3)
four = threading.Thread(target=thred_4)
five = threading.Thread(target=thred_5)


one.start()
two.start()
three.start()
four.start()
five.start()