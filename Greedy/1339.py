n = int(input())

word, length = [], []
for i in range(n):
    s = list(input())
    word.append(s)
    length.append(len(s))
max_length = max(length)

alphabet = dict()
for i in range(n):
    for l in range(length[i]):
        if not word[i][l] in alphabet:
            alphabet[word[i][l]] = 10 ** (length[i] - l - 1)
        else:
            alphabet[word[i][l]] += 10 ** (length[i] - l - 1)

alphabet = dict(sorted(alphabet.items(), reverse = True))
sorted_index = sorted(alphabet, key= lambda x : alphabet[x], reverse=True)

answer, max_num = 0, 9
for s in sorted_index:
    answer += max_num * alphabet[s]
    max_num -= 1

print(answer)