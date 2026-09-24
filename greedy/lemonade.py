bills = [5,5,5,10,20]
# [5,5,5,10,20]

cnt_5 = 0
cnt_10 = 0
cnt_20 = 0
i=0
flag = True
while i < len(bills):
    if bills[i] == 5:
        cnt_5+=1
    elif bills[i] == 10:
        if cnt_5 >= 1:
            cnt_10+=1
            cnt_5-=1
        else:
            flag = False
            break
    elif bills[i] == 20:
        if cnt_10 == 0 and cnt_5 >= 3:
            cnt_5 -= 3
        elif cnt_10 >=1 and cnt_5 >=1:
            cnt_10 -= 1
            cnt_5 -= 1
        else:
            flag = False
            break

    i+=1

if flag == False:
    print("flase")
else:
    print('true')
    
    

