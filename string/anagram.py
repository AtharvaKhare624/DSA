s = "anagram"
t = "nagaram"

freq = {}
for i in s:
    if i not in freq:freq[i] = 1
    else:
        freq[i]+=1

freq2 = {}
for j in t:
    if j not in freq2:freq2[j] = 1
    else:
        freq2[j]+=1

if freq == freq2:
    print(True) 
else:
    print(False)


unqiue = {a for a in s}
print(unqiue)