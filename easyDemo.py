def findNumber(n):
    if n < 10:
        return n
    s = str(n)

    if int(s[0]) > int(s[1]):
        for i in range(1, len(s)-1):
            if int(s[i]) < int(s[i+1]):
                s[i+1] = int(s[i]) - 1
        print(s)
    else:
        for i in range(0, len(s)-1):
            return

    return


findNumber(968)
