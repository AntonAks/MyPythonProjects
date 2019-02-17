s = "aabbcc"
a = "aa"
b = "aaa"

i = 0
while True:
    if a in b and b in a:
        print(0)
        break

    if a in s:
        s = s.replace(a,b)
        i = i + 1
    else:
        print(i)
        break

    if i == 1000:
        print("Impossible")
        break
