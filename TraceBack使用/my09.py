#coding=utf-8
import traceback
try:
    print("step1")
    num = 1/0
except:
    with open("TraceBack使用/a.txt","a") as f:
        traceback.print_exc(file=f)