import textwrap

def wrap(string, max_width):
    wrapped_text=textwrap.wrap(string, max_width)
    rst_str=''
    for i in wrapped_text:
        rst_str = rst_str + i + '\n' 
    return  rst_str


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


