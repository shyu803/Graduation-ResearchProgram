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
            print("")
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
                print(temp)
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
        link[int(i)][0] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link[int(i)][1] = int(input("リンク"+str(i)+"番の接続ノードを入力:"))
        link_r[int(i)] = a
        if(link[int(i)][0]==link[int(i)][1]):
            print("error0")
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
    link_0[12]=[7,10]
    link_0[13]=[1,8]
    link_0[14]=[8,9]
    link_0[15]=[8,9]
    link_0[16]=[9,10]
    link_0[17]=[9,10]
    link_0[18]=[10,11]
    link_0[19]=[10,11]
    link_0[20]=[11,12]
    link_0[21]=[11,12]
    link_0[22]=[12,13]
    link_0[23]=[12,13]
    link_0[24]=[13,20]
    link_0[25]=[1,14]
    link_0[26]=[14,15]
    link_0[27]=[14,15]
    link_0[28]=[15,16]
    link_0[29]=[15,16]
    link_0[30]=[16,17]
    link_0[31]=[16,17]
    link_0[32]=[17,18]
    link_0[33]=[17,18]
    link_0[34]=[18,19]
    link_0[35]=[18,19]
    link_0[36]=[19,20]
    link_0[37]=[0,21]
    link_0[38]=[21,22]
    link_0[39]=[22,23]
    link_0[40]=[22,23]
    link_0[41]=[23,24]
    link_0[42]=[23,24]
    link_0[43]=[24,25]
    link_0[44]=[24,25]
    link_0[45]=[25,26]
    link_0[46]=[25,26]
    link_0[47]=[26,27]
    link_0[48]=[26,27]
    link_0[49]=[27,46]
    link_0[50]=[21,28]
    link_0[51]=[28,29]
    link_0[52]=[28,29]
    link_0[53]=[29,30]
    link_0[54]=[29,30]
    link_0[55]=[30,31]
    link_0[56]=[30,31]
    link_0[57]=[31,32]
    link_0[58]=[31,32]
    link_0[59]=[32,33]
    link_0[60]=[32,33]
    link_0[61]=[33,46]
    link_0[62]=[21,34]
    link_0[63]=[34,35]
    link_0[64]=[34,35]
    link_0[65]=[35,36]
    link_0[66]=[35,36]
    link_0[67]=[36,37]
    link_0[68]=[36,37]
    link_0[69]=[37,38]
    link_0[70]=[37,38]
    link_0[71]=[38,39]
    link_0[72]=[38,39]
    link_0[73]=[39,46]
    link_0[74]=[21,40]
    link_0[75]=[40,42]
    link_0[76]=[40,41]
    link_0[77]=[41,42]
    link_0[78]=[40,42]
    link_0[79]=[42,43]
    link_0[80]=[42,43]
    link_0[81]=[43,44]
    link_0[82]=[43,44]
    link_0[83]=[44,45]
    link_0[84]=[44,45]
    link_0[85]=[45,46]
    link_0[86]=[0,47]
    link_0[87]=[47,48]
    link_0[88]=[48,49]
    link_0[89]=[48,49]
    link_0[90]=[49,50]
    link_0[91]=[49,50]
    link_0[92]=[50,51]
    link_0[93]=[50,51]
    link_0[94]=[51,52]
    link_0[95]=[51,52]
    link_0[96]=[52,53]
    link_0[97]=[52,53]
    link_0[98]=[53,58]
    link_0[99]=[47,54]
    link_0[100]=[54,55]
    link_0[101]=[54,55]
    link_0[102]=[55,56]
    link_0[103]=[55,56]
    link_0[104]=[56,57]
    link_0[105]=[56,57]
    link_0[106]=[56,57]
    link_0[107]=[56,57]
    link_0[108]=[57,58]
    link_0[109]=[57,58]
    link_0[110]=[20,59]
    link_0[111]=[46,59]
    link_0[112]=[58,59]

      
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

link_length = 113
node_length = 60
"""
repeat = link_length
"""
"""
a = float(input("数字a:"))
s = int(input("秘密情報:"))
"""
a =2.3
s = 82822181879
link = {}
link_0 = {}
link_r=[]
link_r_0 = []
node = {}

# 1.グラフ処理
graph1()
## x_num = int(input("リンクXの番号を入力:"))
x_num = 108
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
print("2.xの計算")

# 3.検算
print("検算")
link = link_0.copy()
link_r = link_r_0.copy()
link_r[x_num] = xx[0]
node = {}
graph2()
print(link)
print(node)
print(link_r)
print("x="+str(xx[0]))
print("a="+str(a))
print("s="+str(s))
print("S="+str(link_r[len(link_r)-1]))
sss = "{:.60f}".format(link_r[len(link_r)-1])
print(sss)
hin = "{:.60f}".format(0.1)
print(hin)
elapsed_time0 = time.process_time() - start_time
print(elapsed_time0)


print("リンク数："+str(link_length))
print("Ri="+str(a))
print("シークレットS="+str(s))
print("--計算結果--")
print("Rj="+str(xx[0]))
print("復号されたS="+str(link_r[len(link_r)-1]))
end_time = time.time()
print("計算時間：",str(end_time - start_time)+"秒")