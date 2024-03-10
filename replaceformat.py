def print_full_name(first, last):
    affichage = "Hello {} {} ! You just delved into python."
    return print(affichage.format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)