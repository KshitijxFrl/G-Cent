from LIB.DB import izDB as cdb
from LIB.TOOLS import json_controller as jc

a  = jc.oneTimeCheck()
print(a)


if a == False:
    print('hello')
    cdb.createDB()
    jc.oneTimeEntry()