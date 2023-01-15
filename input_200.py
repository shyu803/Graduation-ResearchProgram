from timeit import repeat
import sympy
import time

start_time = time.time()

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
    length = len(link)
    print("seri"+str(i),length)
    print(node[i],link[node[i][0]],link[node[i][1]],)
    link_r.append(0)
    if(link[node[i][0]][0] != i):
        temp1 = link[node[i][0]][0]
    else:
        temp1 = link[node[i][0]][1]
    if(link[node[i][1]][0] != i):
        temp2 = link[node[i][1]][0]
    else:
        temp2 = link[node[i][1]][1]
    if(temp1<temp2):
        link[length] = [temp1, temp2]
    else:
        link[length] = [temp2, temp1]
    if(node[i][0] in node[link[length][0]]):
        node[link[length][0]].remove(node[i][0])
    if(node[i][1] in node[link[length][0]]):
        node[link[length][0]].remove(node[i][1])
    if(node[i][0] in node[link[length][1]]):
        node[link[length][1]].remove(node[i][0])
    if(node[i][1] in node[link[length][1]]):
        node[link[length][1]].remove(node[i][1])
    node[link[length][0]].append(length)
    node[link[length][1]].append(length)
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
        link_r[int(i)] = a
        if(link[int(i)][0]==link[int(i)][1]):
            print("error0")
        if(link[int(i)][0]>link[int(i)][1]):
            temp = link[int(i)][0]
            link[int(i)][0] = link[int(i)][1]
            link[int(i)][1] = temp
    x_num = 94
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
    link_0[0]=[0,1]
    link_0[1]=[1,2]
    link_0[2]=[2,3]
    link_0[3]=[2,3]
    link_0[4]=[3,4]
    link_0[5]=[3,4]
    link_0[6]=[4,5]
    link_0[7]=[4,5]
    link_0[8]=[5,6]
    link_0[9]=[5,6]
    link_0[10]=[6,7]
    link_0[11]=[6,7]
    link_0[12]=[7,8]
    link_0[13]=[7,8]
    link_0[14]=[8,9]
    link_0[15]=[8,9]
    link_0[16]=[9,10]
    link_0[17]=[9,10]
    link_0[18]=[10,11]
    link_0[19]=[10,11]
    link_0[20]=[11,28]
    link_0[21]=[3,12]
    link_0[22]=[12,13]
    link_0[23]=[12,13]
    link_0[24]=[13,14]
    link_0[25]=[13,14]
    link_0[26]=[14,6]
    link_0[27]=[1,15]
    link_0[28]=[15,16]
    link_0[29]=[15,16]
    link_0[30]=[16,17]
    link_0[31]=[16,17]
    link_0[32]=[16,17]
    link_0[33]=[17,18]
    link_0[34]=[17,18]
    link_0[35]=[17,18]
    link_0[36]=[17,18]
    link_0[37]=[18,19]
    link_0[38]=[18,19]
    link_0[39]=[18,19]
    link_0[40]=[19,20]
    link_0[41]=[19,20]
    link_0[42]=[20,21]
    link_0[43]=[21,28]
    link_0[44]=[1,22]
    link_0[45]=[22,23]
    link_0[46]=[22,23]
    link_0[47]=[23,24]
    link_0[48]=[23,24]
    link_0[49]=[23,24]
    link_0[50]=[24,25]
    link_0[51]=[24,25]
    link_0[52]=[25,26]
    link_0[53]=[25,26]
    link_0[54]=[25,26]
    link_0[55]=[26,27]
    link_0[56]=[26,27]
    link_0[57]=[27,28]
    link_0[58]=[27,28]
    link_0[59]=[28,48]
    link_0[60]=[0,29]
    link_0[61]=[29,30]
    link_0[62]=[30,31]
    link_0[63]=[30,31]
    link_0[64]=[31,32]
    link_0[65]=[31,32]
    link_0[66]=[31,32]
    link_0[67]=[32,33]
    link_0[68]=[32,33]
    link_0[69]=[33,34]
    link_0[70]=[33,34]
    link_0[71]=[33,34]
    link_0[72]=[34,47]
    link_0[73]=[29,35]
    link_0[74]=[35,47]
    link_0[75]=[29,36]
    link_0[76]=[36,37]
    link_0[77]=[36,37]
    link_0[78]=[37,38]
    link_0[79]=[37,38]
    link_0[80]=[37,38]
    link_0[81]=[38,39]
    link_0[82]=[38,39]
    link_0[83]=[38,39]
    link_0[84]=[39,40]
    link_0[85]=[39,40]
    link_0[86]=[40,41]
    link_0[87]=[40,41]
    link_0[88]=[40,41]
    link_0[89]=[41,42]
    link_0[90]=[41,42]
    link_0[91]=[42,47]
    link_0[92]=[29,43]
    link_0[93]=[43,44]
    link_0[94]=[43,44]
    link_0[95]=[44,45]
    link_0[96]=[44,45]
    link_0[97]=[45,46]
    link_0[98]=[46,47]
    link_0[99]=[47,48]
    for i in range(link_length):
        link_r_0.append(0)
        ## link_0[int(i)] = [0,0]
        ## link_0[int(i)][0] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        ## link_0[int(i)][1] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link_r_0[int(i)] = a
        if(link_0[int(i)][0]==link_0[int(i)][1]):
            print("error1")
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
        if(link_r.count(0) == (len(link_r) - 1) or num>200):
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
link_length = 200
node_length = 99
repeat = link_length
a = 2.5
s = 3342
link = {}
link_0 = {}
link_r=[]
link_r_0 = []
node = {}

# 1.グラフ処理
graph1()
x_num = 94
link_r[x_num] = x
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
link_r[x_num] = xx[0]
print(x_num,link_r[x_num],link_r)
node = {}
graph2()
print(link_r[len(link_r)-1])

print("x="+str(xx[0]))

end_time = time.time()
print(start_time,end_time,end_time - start_time)


print("リンク数："+str(link_length))
print("Ri="+str(a))
print("シークレットS="+str(s))
print("--計算結果--")
print("Rj="+str(xx[0]))
print("復号されたS="+str(link_r[len(link_r)-1]))
end_time = time.time()
print("計算時間：",str(end_time - start_time)+"秒")