# Read from standard input and print to standard output
n = int(input())
arr = list(map(int,input().split()))
def solution():
   cost = 0
   for _ in range(len(arr)):
       arr.sort()
       min_sum = arr[0] + arr[1]
       cost = cost + min_sum
       arr.remove(arr[0])
       arr.remove(arr[0])
       arr.append(min_sum)
    print(cost)
solution()