def main():
    data =  [['A','B'],['G','H'],['A','G'],['H','K'],['K','F'],['F','X'],['G','X'],['B','K']]
    myMap = {}
    for node in data:
        myMap[node[0]] = myMap.get(node[0],[])+[node[1]]
        myMap[node[1]] = myMap.get(node[1],[])+[node[0]]
    start = 'A'
    end = 'X'
    shortestPath = bfs(myMap,start,end)
    print(' '.join(shortestPath))

#找到點對點最小的路徑
def bfs(myMap,start,end):
    quene = [[start]]
    while quene:
        nowPath = quene.pop(0)
        lastNode = nowPath[-1]
        if lastNode == end:
            return nowPath
        for nextNode in myMap[lastNode]:
            if nextNode in nowPath:
                continue
            quene.append(nowPath+[nextNode])
    
main()