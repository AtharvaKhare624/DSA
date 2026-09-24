h = [7, 5, 1, 2, 6]
total = 0
def frog(n):
    global total 
    if n == 0:return h[0]
    if n < 0: return float("inf")
    total1, total2 = 0,0
    st1 = abs(h[n] - h[n-1])
    total1 = frog(n-1) + st1
    st2 = abs(h[n] - h[n-2])
    total2 = frog(n-2) + st2

    total += min(total1, total2)
    return total

print(frog(4))