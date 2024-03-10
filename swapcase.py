def swap_case(s):
    new_s = s.swapcase()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)