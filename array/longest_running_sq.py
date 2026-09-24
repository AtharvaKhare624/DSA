nums = [100,4,200,1,3,2]

set_num = set(nums)
max_cnt = 0
for num in set_num:
    if num-1 not in set_num:
        cnt = 1
        cur_num = num
        while cur_num+1 in set_num:
            cnt+=1 
            cur_num = cur_num+1
        max_cnt = max(cnt, max_cnt)

print(max_cnt)