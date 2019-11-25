import copy
import itertools
import time

row=15
#製作[[1or0]...]所有排列組合
def list2_inc(row):
        #start=time.time()
        a=[[1,0]]*row
        ans=list(itertools.product(*a))
        #end=time.time()
        #print(end-start)
        return ans
#判斷[1,0,1,1,0]為(1,2)
def values_clues(list1):
        cc=0
        list1_values=[[]]
        rr=0
        for side in list1:
                side=side+(0,)
                for ii in side:
                        if ii==0:
                                if cc!=0:
                                        list1_values[rr].append(cc)
                                cc=0
                        elif ii==1:
                                cc+=1
                list1_values.append([])
                rr +=1
        #特殊處理會多最後一個且倒數第二0000不會輸出
        #list1_values.pop()
        #list1_values[-1]=[()]
        return list1_values

#dict1_keys_all用clues所需dict1_keys
def dict1_key(clues,dict1_values,dict1_keys_all):
        dict1={}
        dict1_keys=tuple(set(dict1_keys_all))
        for side in clues:
                for clue in side:
                    if clue in dict1:
                            continue
                    for rr,jj in enumerate(dict1_keys_all):
                            if clue==jj:
                                    if clue in dict1:
                                            dict1[clue]+=(dict1_values[rr]),
                                    else:
                                            dict1[clue]=(dict1_values[rr]),
        dict1[()]=(0,)*row,
        return dict1

#dict1、known製作
dict1={}



#用known刪除多餘的dict1
def known_dict(known,dict1_values):
        n=0
        trans=list(zip(*dict1_values))
                
        for tt,tran in enumerate(trans):
                ii=1
                if known[tt]!=-1:
                        continue
                while 0<ii<len(tran):
                        if tran[ii]==tran[ii-1]:
                                ii += 1
                                continue
                        ii=0
                if ii != 0:
                        known[tt]=tran[0]
        ans=[]
        #若同一行值相同 與known相同跟known=-1 皆保留
        for value in dict1_values:
                if all(map(lambda xx,yy:1 if xx==-1 else 1 if xx==yy else 0,known,value)):
                        ans.append(value)
        if len(ans)==1:
                known=list(known)
                return known,ans
        
        return known,ans
                  
#主函式
dict1_values=list2_inc(15)
dict1_keys_all=values_clues(dict1_values)
dict1_keys_all=tuple(tuple(ii) for ii in dict1_keys_all)
def solve(clues):
        knowns=[[-1 for x in range(15)]for y in range(15)]
        #dict1字典只祧clues
        dict1=dict1_key(clues,dict1_values,dict1_keys_all)
        hh,ww=(list(dict1[clue] for clue in side) for side in clues)
        #known -1代表未知
        while not all(map(lambda aa:0 if -1 in aa else 1,knowns)):
                
                for cc,col in enumerate(knowns):
                        knowns[cc],hh[cc]=known_dict(col,hh[cc])
                knowns=list(zip(*knowns))
                knowns=[list(ii) for ii in knowns]
                for rr,row in enumerate(knowns):
                        knowns[rr],ww[rr]=known_dict(row,ww[rr])
                knowns=list(zip(*knowns))                       
                knowns=[list(ii) for ii in knowns]
        return tuple(zip(*knowns))  
        '''全部交叉運算算太慢
        for r in itertools.product(*ww):
                if all(c in hh[i] for i,c in enumerate(zip(*r))):return r'''

clues = (
    (
        (4, 3), (1, 6, 2), (1, 2, 2, 1, 1), (1, 2, 2, 1, 2), (3, 2, 3),
        (2, 1, 3), (1, 1, 1), (2, 1, 4, 1), (1, 1, 1, 1, 2), (1, 4, 2),
        (1, 1, 2, 1), (2, 7, 1), (2, 1, 1, 2), (1, 2, 1), (3, 3)
    ), (
        (3, 2), (1, 1, 1, 1), (1, 2, 1, 2), (1, 2, 1, 1, 3), (1, 1, 2, 1),
        (2, 3, 1, 2), (9, 3), (2, 3), (1, 2), (1, 1, 1, 1),
        (1, 4, 1), (1, 2, 2, 2), (1, 1, 1, 1, 1, 1, 2), (2, 1, 1, 2, 1, 1), (3, 4, 3, 1)
    )
)
clues=(((2,), (1, 1, 3), (2, 2, 3, 1), (1, 1, 1, 3, 3), (1, 1, 1, 3, 1), (2, 4, 2), (2, 1, 4), (6, 1, 1, 1), (2, 1, 1, 1), (2, 1, 1, 1, 1), (1, 2, 2, 3), (1, 2, 1), (4, 1, 2), (4,), ()), ((2,), (1, 2, 2), (1, 1, 2, 2, 1), (2, 1, 1, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 2), (2, 1, 2), (3, 5), (1, 1, 2), (2, 2, 1, 1), (1, 1, 1, 1, 1, 1), (2, 1, 1, 1, 2), (1, 2, 3, 1, 1), (3, 2, 2), (3, 3)))
'''
clues = (((1,), (3,), (1,), (3, 1), (3, 1)),
          ((3,), (2,), (2, 2), (1,), (1, 2)))       '''   
                
        

				

