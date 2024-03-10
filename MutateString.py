
#Version 1: convert a string to a list
def mutate_string(string, position, character):
    l= list(string)
    l[position]= character
    s=''.join(l)
    return s

# Version 2: slice a string to replace a specif character

def mutate_string(string, position, character):

    return string[:position]+character+ string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)