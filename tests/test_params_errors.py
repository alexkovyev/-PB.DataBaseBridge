from DBAccess.DBBridge import dbbridge

bridge = dbbridge.DBBridge()


def test_query_after_error():
    try:
        print(bridge.execute_db_proc_with_params('FN_EncodeInfo', ['123', '123']))
    except:
        pass

    print(bridge.execute_db_proc_with_params('FN_EncodeInfo', ['123']))


def test_proc_without_params():
    print(bridge.execute_db_proc_with_params('FN_GetControllers'))


test_query_after_error()
test_proc_without_params()
