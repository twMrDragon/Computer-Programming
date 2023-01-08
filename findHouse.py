def main():
    houseCount = int(input())
    housePair = {}
    #get house data
    for i in range(houseCount):
        data = input().split()
        housePair[data[0]] = set(data[1:])

    #add filter
    allFilter = []
    filterCount = int(input())
    for i in range(filterCount):
        data = input().split('+')
        orFilter = []
        for j in data:
            orFilter.append(set(removeEmpty(j.split())))
        allFilter.append(orFilter)
    
    #1 符合條件的房屋
    #2 符合最多條件的房屋
    answerSelection = int(input())
    for orFilter in allFilter:
        answerPair = getFilterAns(housePair,orFilter)
        ans = []
        if answerSelection == 0:
            for k,v in answerPair.items():
                if v>0:
                    ans.append(k)
        elif answerSelection == 1:
            target = max(answerPair.values())
            for k,v in answerPair.items():
                if v == target:
                    ans.append(k)
        ans.sort()
        print(' '.join(ans))
            

def getFilterAns(housePair,orFilter):
    answerPair = {}
    for houseName,value in housePair.items():
        count = 0
        for andFilter in orFilter:
            if andFilter<=value:
                count+=1
        answerPair[houseName] = count
    return answerPair

def removeEmpty(data):
    return [i for i in data if data]

main()