import types

def f():
    print("f function")

if type(f) == types.LambdaType:
    print("lambdaType")

if type(f) == types.FunctionType:
    print("functionType")



if type(lambda x:x) == types.LambdaType :
    print("lambdaType")

if type(lambda x:x) == types.FunctionType:
    print("functionType")