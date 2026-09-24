intervals = [[1,4],[4,5]]
overlap = []
result = []
intervals.sort()

for i in range(1,len(intervals)):
    if intervals[i][0] <= intervals[i-1][1]:
        overlap.append(intervals[i])
        if intervals[i-1] not in overlap:
            overlap.append(intervals[i-1])
    else:result.append(intervals[i])

i = 1
newinterval = overlap[0]
while i < len(overlap):
    newinterval[0] = min(newinterval[0], overlap[i][0])
    newinterval[1] = max(newinterval[1], overlap[i][1])
result.append(newinterval)
result.sort()
print(overlap)

# while i<len(intervals) and intervals[i][0] < intervals[i-1][1]:
#     result.append(intervals[i])
