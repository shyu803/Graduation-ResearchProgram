"""
d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}

keys = [k for k, v in d.items() if v == 'aaa']
print(keys)

# ['key1', 'key2']

keys = [k for k, v in d.items()]
print(keys)
# ['key3']

keys = [k for k, v in d.items() if v == 'xxx']
print(keys)
# []
"""
import sympy
# 記号yを定義
x, y, a, b = sympy.symbols('x,y,a,b')

# 多項式zを定義
z = 1.7*x

# xに3, yに5を代入
print(z)
z = z.subs([(x, 3)])
print(z)