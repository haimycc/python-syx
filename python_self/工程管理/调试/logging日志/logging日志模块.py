import logging
#指定显示的日志级别
logging.basicConfig(level=logging.ERROR)

s = '0'
n = int(s)
#记录不同级别的日志
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warn")
logging.error("this is error")
print(10 / n)
