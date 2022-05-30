import sympy
 
# Input the graph
# リンクとノードの数を入力
ss = int(input("秘密情報Sの数字を入力:"))
link_length = int(input("リンクの数を入力:"))

# xを算出
x, y, a, b, s = sympy.symbols('x,y,a,b,s')
a = 2
b = link_length
s = ss
f = (a**(b-1))*x - s
x = sympy.solve(f)
print("x="+str(x[0]))

# sが正しく復号できるか検算
g = float((a**(b-1))*x[0])
print("s="+str(g))

"""
# xを算出(ans)

f = (1-(1-a)*(1-a))*(1-(1-a)*(1-x)) - s
ans = sympy.solve(f)[0]
print(ans)

# sが正しく復号できるか検算
g = (1-(1-a)*(1-a))*(1-(1-a)*(1-ans))
print(g,type(g))
"""