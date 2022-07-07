from timeit import repeat
import sympy

# 関数
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

def graph0():
    for i in range(link_length):
        link_r.append(0)
        link[int(i)] = [0,0]
        link[int(i)][0] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link[int(i)][1] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link_r[int(i)] = a
        if(link[int(i)][0]==link[int(i)][1]):
            print("error")
        if(link[int(i)][0]>link[int(i)][1]):
            temp = link[int(i)][0]
            link[int(i)][0] = link[int(i)][1]
            link[int(i)][1] = temp
    x_num = int(input("リンクXの番号を入力:"))
    link_r[x_num - 1] = x
    print(link)
    print(link_r)
    print(type(link))
    print(x_num)
    print("リンクリスト設定完了")
    num = 0
    while True:
        num += 1
        # 並列チェック
        paraize()
        # 次数チェック
        for i in range(node_length):
            if 0 < i and i < (node_length - 1):
                if(len(node[i]) == 2):
                    serize(i)
        repeat = len(link)
        print("whilelink:"+str(len(link)))    
        print(link_r.count(0),len(link_r))
        if(link_r.count(0) == (len(link_r) - 1) or num>100):
            break
    print("end")
    print(num)
    print(link)
    print(node)
    print(link_r)
    print(link_r[len(link_r)-1])
    print(link_r.count(0),len(link_r))

def graph1():
    global link, link_r
    for i in range(link_length):
        link_r_0.append(0)
        link_0[int(i)] = [0,0]
        link_0[int(i)][0] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link_0[int(i)][1] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link_r_0[int(i)] = a
        if(link_0[int(i)][0]==link_0[int(i)][1]):
            print("error")
        if(link_0[int(i)][0]>link_0[int(i)][1]):
            temp = link_0[int(i)][0]
            link_0[int(i)][0] = link_0[int(i)][1]
            link_0[int(i)][1] = temp
    link = link_0.copy()
    link_r = link_r_0.copy()

def graph2():
    global repeat
    repeat = len(link)
    num = 0
    while True:
        num += 1
        # 並列チェック
        paraize()
        # 次数チェック
        for i in range(node_length):
            if 0 < i and i < (node_length - 1):
                if(len(node[i]) == 2):
                    serize(i)
        repeat = len(link)
        print("whilelink:"+str(len(link)))    
        print(link_r.count(0),len(link_r))
        if(link_r.count(0) == (len(link_r) - 1) or num>100):
            break
    print("end")
    print(num)
    print(link)
    print(node)
    print(link_r)
    print(link_r[len(link_r)-1])
    print(link_r.count(0),len(link_r))

# 0.（初期設定）リンクとノードの数を入力
x, a, s = sympy.symbols('x,a,s')
link_length = int(input("リンクの数を入力:"))
node_length = int(input("ノードの数を入力:"))
repeat = link_length
a = 1.7
s = 10
link = {}
link_0 = {}
link_r=[]
link_r_0 = []
node = {}

# 1.グラフ処理
graph1()
x_num = int(input("リンクXの番号を入力:"))
link_r[x_num - 1] = x
print(link)
print(link_r)
print(type(link))
print(x_num)
print("リンクリスト設定完了")
graph2()

# 2.xの計算
f_0 = link_r[len(link_r)-1]
print(f_0)
f = f_0 - s
xx = sympy.solve(f)
print("x="+str(xx[0]))

# 3.検算
print("検算")
link = link_0.copy()
link_r = link_r_0.copy()
link_r[x_num - 1] = xx[0]
node = {}
graph2()
print(link_r[len(link_r)-1])

print("x="+str(xx[0]))