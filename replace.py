def split_and_join(line):
    r = line.replace(' ', '-')
    return r.strip('-')




if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)