import asyncio
from DBAccess.DBBridge import dbbridge


async def query():
    bridge = dbbridge.DBBridge()
    bridge.execute_db_proc_with_params('FN_GetControllers')


async def query_1():
    bridge = dbbridge.DBBridge()
    bridge.execute_db_proc_with_params('FN_GetControllers')


async def query_2():
    bridge = dbbridge.DBBridge()
    bridge.execute_db_proc_with_params('FN_GetControllers')


async def query_3():
    bridge = dbbridge.DBBridge()
    bridge.execute_db_proc_with_params('FN_GetControllers')


async def query_4():
    bridge = dbbridge.DBBridge()
    bridge.execute_db_proc_with_params('FN_GetControllers')


async def query_5():
    bridge = dbbridge.DBBridge()
    bridge.execute_db_proc_with_params('FN_GetControllers')


asyncio.gather(
    query(),
    query_1(),
    query_2(),
    query_3(),
    query_4(),
    query_5(),
)
