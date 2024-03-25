s = str(input())
final_list = []
i = 0

while i < len(s):
    count = 1
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        count += 1
        j += 1
    final_list.append((count, int(s[i])))
    i = j

print(*final_list)
