#命名关键字参数和关键字参数唯一不同的是，限制了命名参数的key
#不允许我们随便传递key和value过来
#命名关键字参数属于特殊的关键字参数
def function(name,age,*,city, job):
    print(name)
    print(age)
    print(city)
    print(job)

function("zxp",30,city="深圳",job="工程师")