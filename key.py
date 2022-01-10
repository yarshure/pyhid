#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import serial
import control

def doKeys(com):
    print(" - baud_rate:" + str(com.baudrate))  # 波特率
    print(" - byte_size:" + str(com.bytesize))  # 比特大小
    print(" - break_condition:" + str(com.break_condition))  # 校验位

    if com.isOpen():
        print(" - status:OK")
    else:
        print(" - status:FAIL")
        return
def doControl(c):
    c.keyboard_free()
    c.word("yt5n]zh",1)
    c.keyboard(["LEFT_SHIFT","q"],1)
    c.keyboard("ENTER",1)
def doPhone(c):
    c.keyboard_free()
    c.word("281905",1)
if __name__ == "__main__":
    try:
        com = serial.Serial("/dev/cuaU0", 9600, timeout=1)
        print("Open OK")
        doKeys(com)
        
        c = control.Control(com)  # 设置端口
        doPhone(c)
    except serial.serialutil.SerialException as e:
        print(" - Error:" + repr(e))
        #return
