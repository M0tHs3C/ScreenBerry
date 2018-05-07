#!/usr/bin/python
#_*_ coding: utf-8 _*_
import os
#("C:\\Users\\ALESSANDROGIBERTONI\\Desktop\\ScreenBerry\\time.conf", "r").read().splitlines()
target_host = "192.168.4.256:123"
a = open("C:\\Users\\ALESSANDROGIBERTONI\\Desktop\\ScreenBerry\\screenberry.conf", "r").read().splitlines()
if target_host in a:
    print"già salvata"


