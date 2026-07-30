N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
handshakes.sort()


clap=[0 for _ in range(N+1)]
contaminate=[0 for _ in range(N+1)]
contaminate[P]=1

for elem in handshakes:
    if all(contaminate[_]==0 for _ in elem[1:]):
        pass
    elif all(contaminate[_]==1 for _ in elem[1:]):
        if all(clap[_]==K for _ in elem[1:]):
            pass
        elif all(clap[_]<K for _ in elem[1:]):
            for _ in elem[1:]:
                clap[_]+=1
        elif any(clap[_]==K for _ in elem[1:]):
            for _ in elem[1:]:
                if clap[_]<K:
                    clap[_]+=1
    elif any(contaminate[_]==1 for _ in elem[1:]): 
        for _ in elem[1:]:
            if contaminate[_]==1 and clap[_]==K:
                pass
        if contaminate[elem[1]]==0 and clap[elem[2]]<K:
            contaminate[elem[1]]=1
            clap[elem[2]]+=1
        elif contaminate[elem[1]]==1 and clap[elem[1]]<K:
            contaminate[elem[2]]=1
            clap[elem[1]]+=1

for elem in contaminate[1:]:
    print(elem,end="")