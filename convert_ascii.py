x = "\u042d\u0442\u043e"
print(len(x), x, type(x))
# 3
y = x.encode('ascii', 'backslashreplace')
# y
# b'\\u042d\\u0442\\u043e'
print(len(y), y, type(y))
# 18

new_x = y.decode('ascii', 'backslashreplace')
print(len(new_x), new_x, type(new_x))

new_x = new_x.encode('utf-8', 'backslashreplace')
print(len(new_x), new_x, type(new_x))