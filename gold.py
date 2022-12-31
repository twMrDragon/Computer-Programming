def main():
    # gold = list(map(int,input().split()))
    gold = [1,2,3,4,5]
    # maxGoldCount = int(input())
    maxGoldCount = 3
    maxGoldWeight = sum(gold)//3
    ans = []

    def dfs(stillHave,everyoneCount):
        for i in everyoneCount:
            #超過最大數量
            if len(i)>maxGoldCount:
                return
            #超過平均分配重量
            if sum(i)>maxGoldWeight:
                return

        #找到答案
        if not stillHave:
            ans.append(everyoneCount)
            return

        nextAdd = stillHave[0]
        nextStillHave = stillHave[1:]
        #遞迴嘗試每種組合
        for i in range(len(everyoneCount)):
            nextEveryoneCount = [value2+[nextAdd] if index2 == i else value2+[] for index2,value2 in enumerate(everyoneCount)]
            dfs(nextStillHave,nextEveryoneCount)

    dfs(gold,[[],[],[]])
    for i in ans:
        print(i)
    print(len(ans))
main()