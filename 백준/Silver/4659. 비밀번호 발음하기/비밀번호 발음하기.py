def check_vowel(word):
    cnt = 0
    for i in range(len(word)):
        if word[i] in vowel:
            cnt += 1
    if cnt == 0:
        return True
    return False

def check_triple(word):
    v_cnt = 0
    c_cnt = 0
    for i in range(len(word)):
        if word[i] in vowel:
            v_cnt += 1
            c_cnt = 0
            if v_cnt == 3:
                return True
        else:
            c_cnt += 1
            v_cnt = 0
            if c_cnt == 3:
                return True
    return False

def check_double(word):
    tmp = 1
    for i in range(len(word)-1):
        if word[i] == word[i+1] and word[i] != 'e' and word[i] != 'o':
            tmp += 1
        if tmp == 2:
            return True
    return False

vowel = ['a','e','i','o','u']
while True:
    word = input()
    if word == "end":
        break

    if check_vowel(word) or check_triple(word) or check_double(word):
        print("<"+word+">","is not acceptable.")
        continue

    print("<"+word+">","is acceptable.")