#從左上角開始 初始值為0 往右+2 往左-2 往上/ 2 往下*2
import copy
'''
list1=[[1,5],[0,2,6],[1,3,7],[2,4,8],[3,9],[0,6,10],[1,5,7,11],[2,6,8,12],[3,7,9,13],[4,8,14],[5,11,15],[6,10,12,16],[7,11,13,17],[8,12,14,18],[9,13,19],[10,16,20],[11,15,17,21],[12,16,18,22],[13,17,19,23],[14,18,24],[15,21],[16,20,22],[17,21,23],[18,22,24],[19,23]]
aa=0
list2=[]
number=4
def run1(aa,list2):
    list2.append(aa)
    if aa==24:
        #print(list2)
        return print("結束")
    
    list1_new=copy.deepcopy(list1)
    for bb in list1_new[aa]:
        list1[aa].remove(bb)
        list1[bb].remove(aa)
        run1(bb,list2)
        #print(list2[-1],"是死路")
        list2.pop(-1)
        #print(list2)
        list1[aa].append(bb)
        list1[bb].append(aa)
'''
#一開始往右走兩個 初始值為4

list1=[[5],[6],[3,7],[2,4,8],[3,9],[0,6,10],[1,5,7,11],[2,6,8,12],[3,7,9,13],[4,8,14],[5,11,15],[6,10,12,16],[7,11,13,17],[8,12,14,18],[9,13,19],[10,16,20],[11,15,17,21],[12,16,18,22],[13,17,19,23],[14,18,24],[15,21],[16,20,22],[17,21,23],[18,22,24],[19,23]]
aa=2
list2=[]
number=4
def run1(aa,list2,number):
    list2.append(aa)
    if aa==24:
        if number <= 0:
            print(list2,number)
        return 0
    
    list1_new=copy.deepcopy(list1)
    for bb in list1_new[aa]:
        if bb == aa+1:
            number+=2
        elif bb== aa-1:
            number-=2
        elif bb == aa+5:
            number*=2
        elif bb == aa-5:
            number/=2
        list1[aa].remove(bb)
        list1[bb].remove(aa)
        run1(bb,list2,number)
        #print(list2[-1],"是死路")
        list2.pop(-1)
        #print(list2)
        list1[aa].append(bb)
        list1[bb].append(aa)
        if bb == aa+1:
            number-=2
        elif bb== aa-1:
            number+=2
        elif bb == aa+5:
            number/=2
        elif bb == aa-5:
            number*=2
'''    
import copy
list1=[[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
aa=0
list2=[]
def run2(aa,list2):
    list2.append(aa)
    if aa==8:
        print(list2)
        return print("結束")
    
    list1_new=copy.deepcopy(list1)
    for bb in list1_new[aa]:
        list1[aa].remove(bb)
        list1[bb].remove(aa)
        run2(bb,list2)
        #print(list2[-1],"是死路")
        list2.pop(-1)
        #print(list2)
        list1[aa].append(bb)
        list1[bb].append(aa)
'''
