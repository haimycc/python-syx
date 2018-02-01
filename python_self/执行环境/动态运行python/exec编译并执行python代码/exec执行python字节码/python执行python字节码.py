
#注意tab和空格影响编译
code=compile("""
x=0
print("x is currently :",x)
while x<5 :
    x+=1
    print("increamenting x to :",x)

""","","")

exec(code)