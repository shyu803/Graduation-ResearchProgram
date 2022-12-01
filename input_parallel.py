import sympy
 
# Input the graph
# リンクとノードの数を入力
link_length = int(input("リンクの数を入力:"))
node_length = int(input("ノードの数を入力:"))

#リンク定数a、秘密情報Sを入力
x, y, a, b, s = sympy.symbols('x,y,a,b,s')
a= 1.7
s = 10
b = link_length

# 各リンクごとの接続ノードを入力
link = {}
for i in range(link_length):
    link[int(i)] = [0,0,1,0]
    link[int(i)][0] = int(input("リンク"+str(i+1)+"番の接続ノードを入力:"))
    link[int(i)][1] = int(input("リンク"+str(i+1)+"番の接続ノードを入力:"))
x_num = int(input("リンクxの番号を入力:")) - 1
print(x_num)
for i in range(link_length):
    print(i)
    if(i == x_num):
        if( link[int(i)][2] == 1):
            link[int(i)][3] = x
        else:
            link[int(i)][3] = 1 - (((1-a) ** (link[int(i)][2] - 1)) * (1 - x))
    else:
        if( link[int(i)][2] == 1):
            link[int(i)][3] = a
        else:
            link[int(i)][3] = 1 - ((1-a) ** link[int(i)][2])
print(link)

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
f = 1
for i in range(link_length):
    f = f * link[int(i)][3]
f = f - s
print(f)
x = sympy.solve(f)
print("x="+str(x[0]))


# sが正しく復号できるか検算
link[int(x_num)][3] = 1 - (((1-a) ** (link[int(x_num)][2] - 1)) * (1 - x[0]))
g = 1
for i in range(link_length):
    g = g * link[int(i)][3]
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