def insane_cls(max_n, max_fn):
    ans=0
    if max_n==1:
        return max_fn//2+1
    tuples1=insane_two(max_fn)
    print(tuples1)
    for ii in range(max_fn+1):
        print(ii,"開頭")
        ans=insane_find_back(ii,max_n-1,tuples1,ii,ans)
    return ans

#輸入num，若lists1=[[0,0],[0,1],[1,0]]，若第一個數字為0，下一個數為0 跟 1
def insane_find_back(num,count_compute,tuples1,first_num,ans):
    if count_compute == 0:
        if (first_num,num) in tuples1:
            ans+=1
            print("ans",ans)
        return ans
    for tuple1 in tuples1:
        print("tuple1",tuple1,"compute:",count_compute)
        if tuple1[0]==num:
            ans=insane_find_back(tuple1[1],count_compute-1,tuples1,first_num,ans)
    return ans

#找任意兩個數加起來<=max_fn
def insane_two(max_fn):
    tuples1=((),)
    for all_fn in range(max_fn+1):
        #找任意兩個數加起來=max_fn
        for ii in range(0,all_fn+1):
            add=(ii,all_fn-ii),
            tuples1=tuples1+add
    tuples1=tuples1[1::]
    return tuples1
