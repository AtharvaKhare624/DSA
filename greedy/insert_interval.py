arr = [[1,2],[3,4],[5,7],[8,10],[12,16]]
new = [6,8]
result = []
overlap = []
overlap.append(new)
for i in arr:
    start, end = i[0] ,i[1]
    if end < new[0]:
        result.append(i)
    elif start > new[1]:
        result.append(i)
    if end <= new[1] and end >= new[0] or start <= new[1] and start >= new[0]:
        overlap.append(i)

start = overlap[0][0]
end = overlap[0][1]

for i in range(1,len(overlap)):
    start = min(start,overlap[i][0])
    end = max(end,overlap[i][1])
result.append([start,end])

result.sort()
print(result)

i,n=0,len(arr)
while i < n and arr[i][1]<newInterval[0]:
    result.append(arr[i])
    i+=1
while i<n and arr[i][0]<=newInterval[1]:
    newInterval[0]=min(newInterval[0],arr[i][0])
    newInterval[1]=min(newInterval[1],arr[i][1])
    i+=1
while i<n:
    result.append(arr[i])
    