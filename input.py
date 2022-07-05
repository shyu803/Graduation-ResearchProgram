from timeit import repeat
import sympy

isEnd = False
 # 重複検知
def paraize():
    link1 = link.copy()
    for l in range(node_length):
        node[int(l)] = []
    for i in range(repeat):
        print("----")
        print(i) # 数字
        linki = link[i]
        if(i not in link1 or linki[0] == -1):
            print("存在しない")
        else:
            link1.pop(i)
            print(linki)
            print(link1) 
            print(linki in link1.values())
            if(linki in link1.values()):
                link2 = link1.copy()
                k = 1
                temp = 1
                for j in link2:
                    if(linki == link2[j]):
                        k = k + 1
                        link1.pop(j)
                        link[j] = [-1,0]
                        temp = (1-link_r[j]) * temp
                        link_r[j] = 0
                length = len(link)
                link[length] = linki
                link_r.append(0)
                link_r[length] = 1 - (temp * (1 - link_r[i]))
                link[i] = [-1,0]
                link_r[i] = 0
                node[link[length][0]].append(length)
                node[link[length][1]].append(length)
                print("重複:"+str(k)+str(linki))
            else:
                print("ノード"+str(i))
                node[linki[0]].append(i)
                node[linki[1]].append(i)
        print("----")
    print(link)
    print(link_r)    
    print(node)

def serize(i):
    print("seri"+str(i))
    length = len(link)
    link_r.append(0)
    if(link[node[i][0]][0] != i):
        link[length] = [link[node[i][0]][0], link[node[i][1]][1]]
        node[link[length][0]].remove(node[i][0])
        node[link[length][0]].append(length)
        node[link[length][1]].remove(node[i][1])
        node[link[length][1]].append(length)        
    else:
        link[length] = [link[node[i][1]][0], link[node[i][0]][1]]
        node[link[length][1]].remove(node[i][0])
        node[link[length][1]].append(length)
        node[link[length][0]].remove(node[i][1])
        node[link[length][0]].append(length) 
    link_r[length] = link_r[node[i][0]] * link_r[node[i][1]]
    print(node[i],link[length],link_r[length])
    link[node[i][0]] = [-1, 0]
    link[node[i][1]] = [-1, 0]
    link_r[node[i][0]] = 0
    link_r[node[i][1]] = 0

    # node[link[length][0]] = [length if i == node[i][0] else i for i in node[link[length][0]]]
    # node[link[length][1]] = [length if i == node[i][1] else i for i in node[link[length][1]]]
    node[i] = []
    print(link)
    print(link_r)
    print(node)

# Input the graph
# 0.リンクとノードの数を入力
link_length = int(input("リンクの数を入力:"))
node_length = int(input("ノードの数を入力:"))
repeat = link_length

# 0.リンク定数a、秘密情報Sを入力
x, y, a, b, s = sympy.symbols('x,y,a,b,s')
a= 1.7
s = 10
b = link_length

# 1.各リンクごとの接続ノードを入力
link = {}
link_r=[]
node = {}
for i in range(link_length):
    link_r.append(0)
    link[int(i)] = [0,0]
    link[int(i)][0] = int(input("リンク"+str(i+1)+"番の接続ノードを入力:"))
    link[int(i)][1] = int(input("リンク"+str(i+1)+"番の接続ノードを入力:"))
    link_r[int(i)] = a
    if(link[int(i)][0]==link[int(i)][1]):
        print("error")
    if(link[int(i)][0]>link[int(i)][1]):
        temp = link[int(i)][0]
        link[int(i)][0] = link[int(i)][1]
        link[int(i)][1] = temp
print(link)
print(link_r)
print(type(link))
## リンクリスト設定完了

# 並列チェック
paraize()

num = 0
while True:
    num += 1
    repeat = len(link)
    # 次数チェック
    for i in range(node_length):
        if 0 < i and i < (node_length - 1):
            if(len(node[i]) == 2):
                serize(i)
    paraize()
    print(link_r.count(0),len(link_r))
    if(link_r.count(0) == (len(link_r) - 1) or num>100):
        break

print("end")
print(num)
print(link)
print(node)
print(link_r)
print(link_r.count(0),len(link_r))


"""
# xを算出
m = link_length
n = link_length
j = 0
f = 1
for i in range(link_length):
    f = f * link[int(i)][3]
f = f - s
print(f)
x = sympy.solve(f)
print("x="+str(x[0]))


# sが正しく復号できるか検算
g = 1
for i in range(link_length):
    g = g * link[int(i)][3]
print("s="+str(g))


# xを算出(ans)

f = (1-(1-a)*(1-a))*(1-(1-a)*(1-x)) - s
ans = sympy.solve(f)[0]
print(ans)

# sが正しく復号できるか検算
g = (1-(1-a)*(1-a))*(1-(1-a)*(1-ans))
print(g,type(g))
"""