s = "rabbbit"
t = "rabbit"
store = []
for a in s:
    store.append(a)
print(store)
cnt = 0
n = len(s)-1
def subseq(i, st, t):
    global cnt
    if i > n:
        if st == t:
            cnt += 1
        return
    
    st += store[i]
    subseq(i+1, st, t)
    st = st[:-1]
    subseq(i+1, st, t)

st = ""
i = 0
subseq(i, st, t)
print(cnt)