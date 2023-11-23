s = "tar"
t = "rat"

dic1 ={}
dic2 ={}

for _ in range(len(s)):
    c = s[_]
    if c in dic1:
        dic1[c] +=1
    else:
        dic1[c] = 1

for _ in range(len(t)):
    c = t[_]
    if c in dic2:
        dic2[c] +=1
    else:
        dic2[c] = 1

print(dic1)
print(dic2)


for i in range(len(s)):
    c = s[i]
    if dic1.get(c,-1) != dic2.get(c,-1):
        print("ERRORSZ")
print("FINEETO")
