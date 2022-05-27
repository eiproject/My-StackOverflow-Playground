VAR = 123

def func(param=False):
    global VAR
    if param:
        VAR = 456
    return VAR

z = func()
a = func(True)  # 456
b = func()      # UnboundLocalError: ..
print()