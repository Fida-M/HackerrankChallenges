def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
            print(kevin_score)
        else:
            stuart_score += length - i
            print(stuart_score)

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

# Test the function with the sample input
minion_game("BANANA")

