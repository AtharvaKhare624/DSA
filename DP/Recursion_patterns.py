arr = [3,7,5,2,6,8]
# PRINT ALL SUBSEQUENCES
# def subsequence(n,lst, summ):
#     if n == len(arr):
#         if summ == k:
#             print(lst)
#         return 

#     lst.append(arr[n])
#     summ += arr[n]
#     subsequence(n+1, lst, summ)

#     lst.pop()
#     summ -= arr[n]
#     subsequence(n+1, lst, summ)

# PRINT ONLY ONE SUBSEQUENCE
# def subsequence(n, lst,summ):
#     if n == len(arr):
#         if summ == k and True:
#             print(lst)
#             return True
#         return False
#     lst.append(arr[n])
#     summ += arr[n]
#     if subsequence(n+1,lst,summ) == True : return True 
#     lst.pop()
#     summ -= arr[n]
#     if subsequence(n+1,lst, summ) == True : return True
#     return False

# PRINT SUBSEQUENCES COUNT

def subsequence(n, lst):
    if n == len(arr):
        
summ = 0
k = 7
lst = []
subsequence(0, lst, summ)