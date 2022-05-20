import sympy
 
# 変数宣言（x,a,sが利用できるように）
x, y, a, s = sympy.symbols('x,y,a,s')
a = 1.7
s = 154656342345469

'''
＜メモ＞
16桁を超えるとおかしくなる？？？
q = 1234567890123456
'''


# xを算出(ans)
f = (1-(1-a)*(1-a))*(1-(1-a)*(1-x)) - s
ans = float(sympy.solve(f)[0])
print(ans,type(ans))

# sが正しく復号できるか検算
g = float((1-(1-a)*(1-a))*(1-(1-a)*(1-ans)))
k = 0.1*10
print(g,type(g),k)