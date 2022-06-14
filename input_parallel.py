import sympy
 
# Input the graph
# リンクとノードの数を入力
link_length = int(input("リンクの数を入力:"))
node_length = int(input("ノードの数を入力:"))

# 各リンクごとの接続ノードを入力
link = {}
for i in range(link_length):
    link[int(i)] = [0,0]
    link[int(i)][0] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
    link[int(i)][1] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
    
print(link)
print(type(link))

m = link_length
n = link_length
j = 0

for i in range(m):
    for j in range(n):
        if(str(link[int(i)]).count(str(link[int(j)])) and i != j and i <= j):
            print(str(i)+str(j)+"SOMETHING"+str(link[int(i)]))
        else:
            print(str(i)+str(j)+"NOTHING"+str(link[int(i)])+str(link[int(j)]))

# xを算出
x, y, a, b, s = sympy.symbols('x,y,a,b,s')
a = 1.7
b = link_length
s = 30
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