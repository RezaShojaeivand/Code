# Word Count
ftask = open('task.txt')

di = dict()

for line in ftask :
    line = line.rstrip()
    wds = line.rsplit()
    
    for wrd in wds :
        di[wrd] = di.get(wrd,0) + 1

mostRepeted = -1
theword = None
sumv = 0
tmp = list()

for k,v in di.items() :
    tmp.append((v,k))
    if v > mostRepeted :
        mostRepeted = v
        theword = k
    sumv += v
    
tmp = sorted(tmp, reverse=True)
for v,k in tmp[:10] :
    print(k,v)

#print(sorted([ (v,k) for k,v in di.items() ]))
print('\n********************************\n')
print(f'Task include: {sumv} words')
print('The most repeted word is: '
        ,theword,'==>',mostRepeted)
