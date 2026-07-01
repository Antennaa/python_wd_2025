# 作者: Antenna
# 2026年06月01日16时36分23秒
# Antenna2000@163.com
import re

def simple():
    result = re.match('github','github.com')
    if result:
        print(result.group())

def single():
    """
    匹配单个字符
    :return:
    """
    ret = re.match(".", "M")
    print(ret.group())
    ret = re.match("t.o", "too")
    print(ret.group())
    ret = re.match("t.o", "two")
    print(ret.group())
    



if __name__ == '__main__':
    simple()
    print("-"*88)
    single()