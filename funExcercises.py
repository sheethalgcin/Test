'''function for some excercises'''

def removeDuplicateString(words):
    str1 =set(words)
    return str1

def strcompare(words,words2):
    flag = 0
    if len(words) != len(words2):
        print("entered strings does not match")
        return
    else:
        i=0
        while(i < len(words2)):
            if words[i] == words2[i]:
                i = i + 1

            else:
                flag = 1
                break
        if flag:
            print("entered strings does not match")
        else:
            print("entered strings does match")


def freqCharacters(words):
    l = len(words)
    ch = ''
    cntCh = {}
    for ch in words:

        if ch not in cntCh:
            cntCh[ch] = 1
        else:

            cntCh[ch]= cntCh[ch] + 1

    print(cntCh.items())
    for ch, count in cntCh.items():
        print(ch, '--->', count)


str2 = input("enter the string")
str1 = input("enter another string to be compared")
words = str2.split()
words2 =str1.split()
print(removeDuplicateString(words))
strcompare(words,words2)
freqCharacters(words)