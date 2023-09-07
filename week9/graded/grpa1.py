words = []


def constructWord(word: str, subs, temp = []):
    if word == "":
        words.append(temp)
        return [[]]

    for i in subs:
        if word.startswith(i):
            #print(word, i)
            copy = temp.copy()
            copy.append(i)
            x = constructWord(word.replace(i, ""), subs, temp=copy)
            if not x and len(x) > len(subs):
                #print(x, temp)
                words.append(x)
    return words