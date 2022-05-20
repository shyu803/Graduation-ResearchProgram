import sympy
 
# Input the graph
# リンクとノードの数を入力
link_length = input("リンクの数を入力:")
node_length = input("ノードの数を入力:")

# 各リンクごとの接続ノードを入力
link = {}
for i in range(int(link_length)):
    link[int(i)] = [0,0]
    link[int(i)][0] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
    link[int(i)][1] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
    
print(link)

# xを算出
x, y, a, b, s = sympy.symbols('x,y,a,b,s')
a = 1.7
b = int(link_length)
s = 30
f = a^(int(b)-1)*x - s
ans = sympy.solve(f)[0]
print("信頼性は"+ans)

"""
# xを算出(ans)

f = (1-(1-a)*(1-a))*(1-(1-a)*(1-x)) - s
ans = sympy.solve(f)[0]
print(ans)

# sが正しく復号できるか検算
g = (1-(1-a)*(1-a))*(1-(1-a)*(1-ans))
print(g,type(g))
"""