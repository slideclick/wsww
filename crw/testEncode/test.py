# windows 上面你 python test.py '你好' 它会把两个引号当成raw内容传进去 linux不传
import sys 

str = sys.argv[1] 
print(str)
print(len(str)) 
print(type(str)) 
if str == "'你好'": 
    print("ok") 
print('你好'.encode('utf-8')) 
print(str.encode('utf-8')) 

#https://www.v2ex.com/t/352585#reply13
