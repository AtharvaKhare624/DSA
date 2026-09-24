s =[5,6,7,8]
g =[10,9,8,7]
s.sort()
g.sort()

mini = min(len(g), len(s))

j ,i= 0,0
while i < mini and j<mini:
    if g[i] <= s[j]:
        j+=1
        i+=1
    elif g[i] > s[j]:
        j+=1

print(i)