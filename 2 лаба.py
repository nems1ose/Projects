s1 = str(input())
s2 = str(input())
if len(s1) < len(s2):
    s1, s2 = s2, s1
s3 = s1
s1 = '0' + s1
a = [0] * len(s2)
b = [0] * len(s2)
for i in range (0, len(s2)):
    a[i] = i+1
for i in range (1, len(s1)):
    for j in range (0, len(s2)):
        if s2[j] == s1[i]:
            if j == 0:
                b[j] = min(a[j]+1, i+1, i-1)
            else:
                b[j] = min(a[j]+1, b[j-1]+1, a[j-1])
        else:
            if j == 0:
                b[j] = min(a[j]+1, i+1, i)
            else:
                b[j] = min(a[j]+1, b[j-1]+1, a[j-1]+1)
    for j in range (0, len(s2)):
        a[j] = b[j]
print("для слов ", s3 , " и ", s2, " необходимо ", b[len(s2)-1], " преобразован(ие/ия/ий)",) 
