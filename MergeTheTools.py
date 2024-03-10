def merge_the_tools(string,k):
    s=[]
    j=0
    i=k
    final_list=[]
    new_s=''
    while i <= len(string)+1:
        s.append(string[j:i]) 
        i+=k
        j+=k
        
    for x in s:
        string2 =""
        for c in x :
            if c not in string2:
                string2 +=c
        final_list.append(string2)

    return [print(k) for k in final_list] 

if __name__ == '__main__' :
    string, k = input(), int(input())
    merge_the_tools(string, k)

