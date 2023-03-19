"""
用法一

在字符串中插入变量的值，可在前引号前加上字母f，再将要插入的变量放在花括号内。

示例一

first_name="ada"

last_name="lovelace"

full_name=f"{first_name}{last_name}"

print(f"Hello,{full_name.title()}") #备注：title()返回“标题化”后的字符串：将所有单词以答谢开头，其他为小写

打印结果为

Hello，Ada Lovelace!

用法二

使⽤f字符串来创建消息，再把整条消息赋给变量.

示例二first_name="ada"

last_name="lovelace"

full_name=f"{first_name}{last_name}"

message=f"Hello,{full_name.title()}"

print(message)

打印结果为：

Hello，Ada Lovelace!
"""