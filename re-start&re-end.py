import re

s=input() 
k=input()
pattern= re.compile(k)
search = pattern.search(s)
print(search)
if not search:
    print("(-1,-1)")
else:
    while search:
        print(f"({search.start()},{search.end()-1})")
        search=pattern.search(s,search.start()+1)
