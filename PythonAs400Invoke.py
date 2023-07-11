# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 05:41:28 2023

@author: kmod1567
"""

import pyodbc

def convertlentostrformat(cmd):
    cmdlen = str(len(cmd))
    lenoflen = len(cmdlen)
    size=10
    strtest=""
    while size > lenoflen:
        strtest=strtest+"0"
        size=size-1
    strtest=strtest+cmdlen
    strtest = "{}{}".format(strtest, ".00000")
    return strtest


RPGProgram=input("Enter Program Name: ")
param1=input("Enter param1: ")
param2=input("Enter param2: ")

try:
    connection = pyodbc.connect(
            driver='{iSeries Access ODBC Driver}',
            system='ServerName',
            uid='Username',
            pwd='Password')
    
    con = connection.cursor()
        
    cmd = 'CALL  PGM('+RPGProgram+') PARM(\''+param1+'\' \''+param2 +'\')'
    
    print(cmd)
    strtest=convertlentostrformat(cmd)
        
    pgv = "CALL QSYS.QCMDEXC(\'"+cmd.replace("'", "''")+"\',"+strtest+")"
    print(pgv)
    
    con.execute(pgv)
    
    con.close()
    connection.close()
except pyodbc.Error as ex:
    print("error:"+str(ex))
