from collections import Counter
n,m =input().split()
a=[]
b=[]
for _ in range(int(n)):
    a.append(str(input()))
for _ in range(int(m)):
    b.append(str(input()))

l=[]
for i in b:   
    index_word=[]
    if a.count(i)!=0:
        for c in range(len(a)):
            if a[c] == i:
                index_word.append(c+1)
            else:
                pass  
    else:
        index_word.append(-1)   

    l.append(index_word)
for c in l:
    print(*c)