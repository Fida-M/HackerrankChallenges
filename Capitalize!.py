def solve(s):
    l = s.split(' ')
    final_string = ""
    for i in l:
        final_string += i.capitalize() + " "
    return final_string.strip()
p_out=solve("hello   world ")
print(p_out)
