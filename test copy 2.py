"""
l = {}
l[0] = [2, 1, 3]
l[1] = [7, 5, 3]
l[2] = [1, 2, 3]
print(l)
ll = set(l[0]) == set(l[2])
print(ll)
"""
a = 6
s = 10

# 重複検知
def paraize():
    link1 = link.copy()
    for i in range(link_length):
        print(i) # 数字
        if(i not in link1):
            print("存在しない")
        else:
            linki = link[i]
            link1.pop(i)
            print(linki) # 
            print(link1) 
            print(linki in link1.values())
            if(linki in link1.values()):
                link2 = link1.copy()
                k = 1
                for j in link2:
                    if(linki == link2[j]):
                        k = k + 1
                        link1.pop(j)
                        link[j] = [-1,0,0]
                length = len(link)
                link[length] = linki
                print("重複:"+str(k)+str(linki))
                link[length][2] = 1 - ((1 - a)**k)
                link[i] = [-1,0,0]
        print("----")
    print(link)

link_length = 5
link = {}
for i in range(link_length):
    link[int(i)] = [0,0,0]
    link[int(i)][0] = int(input("リンク"+str(i+1)+"番の接続ノードを入力:"))
    link[int(i)][1] = int(input("リンク"+str(i+1)+"番の接続ノードを入力:"))
    link[int(i)][2] = a
    if(link[int(i)][0]==link[int(i)][1]):
        print("error")
    if(link[int(i)][0]>link[int(i)][1]):
        temp = link[int(i)][0]
        link[int(i)][0] = link[int(i)][1]
        link[int(i)][1] = temp
print(link)
print(type(link))
paraize()

