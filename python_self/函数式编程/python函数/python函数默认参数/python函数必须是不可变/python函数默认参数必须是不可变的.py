#list不是不可变的,所以每次调用都会增加1
def function(list=[]):
    list.append(1)
    print(list)

function()
function()
function()