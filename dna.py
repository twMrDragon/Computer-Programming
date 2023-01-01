def main(dna):
    start = 0
    leftTargets = ['ATG']
    rightTargets = ['TAG','TAA','TGA']
    ans = []

    while True:
        leftIndex = findMinIndex(dna,start,leftTargets)
        rightIndex = findMinIndex(dna,leftIndex+3,rightTargets)
        if leftIndex == -1 or rightIndex == -1:
            break
        middle = dna[leftIndex+3:rightIndex]
        if iscorrect(middle):
            ans.append(middle)
        start = min(leftIndex,rightIndex)+3
    
    return ans

def iscorrect(dna):
    notInclude =  ['ATG','TAG','TAA','TGA']
    if len(dna) == 0:
        return False
    if len(dna)%3!=0:
        return False
    for target in notInclude:
        if dna.find(target) != -1:
            return False
    return True

def findMinIndex(dna:str,start,targets):
    ans = -1
    for target in targets:
        index = dna.find(target,start)
        if ans == -1:
            ans = index
        elif index != -1:
            ans = min(ans,index)
    return ans

data = [
    'CCATGTTTTAACCATGCCTAAATGGGGCGTTAGTT',
    'TAAGATGAATGA',
    'ATGAAATGA',
    'ATGTGAATGAAATGA',
    'TTATGTTAAAAGGATGTTAATGTAAGGGCGTTAGTT',
    'AATAGATGTTTAAGTGATATGGGGATGTCATAGATGCCCTTCACCTAA'
]

for i in data:
    ans = main(i)
    print('\n'.join(ans))
    print('-'*30)