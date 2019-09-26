#coding=utf-8
'''
try-except
try:
    f = open("ad.txt","r")
    content = f.readline()
    print(content)
except:
    print("文件未找到")
finally:
    print("关闭资源")
    try:
        f.close()
    except BaseException as e:
        print(e)
'''
#with
"""with open("/Users/liyaolin/Documents/GitHub/Python-note/with管理上下文/ad.txt","r") as f:
    content = f.readline()
    print(content)
print("程序结束")"""
