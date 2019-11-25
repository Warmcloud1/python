#困難點:
#尋找所有符合tip=3的可能 (1,1,1,-1,-1),(-1,1,1,1,-1),(-1,-1,1,1,1)
#集合(1,1,1,-1,-1),(-1,1,1,1,-1),(-1,-1,1,1,1)->(-1,-1,1,-1,-1)找尋1跟0集合 註:-1代表不確定
#直橫二維矩陣
import itertools

class Nonogram:

    def __init__(self, clues,row=5,col=5):
        self.clues=clues
        self.NxN=[[-1]*row]*col
        
    def all_possible(self,known,tip,row=5):
        
        all_onezero=[0 if ii>=sum(tip) else 1 for ii in range(row)]
        all_permutation=list(set(itertools.permutations(all_onezero,row)))
        #known
        known_permutation=[]
        for every_permutation in all_permutation:
            if (all(map(lambda ee,kk:1 if kk==-1 else 1 if ee==kk else 0,every_permutation,known))):
                known_permutation.append(every_permutation)
        #所有可能與known做刪除
        return_all_permutation=[]
        for tip_permutation in known_permutation:
            tmp_permutation=[]
            tmp=[]
            ii=0
            while ii < row:
                if tip_permutation[ii]==0:
                    ii=ii+1
                    continue
                cc=0
                while ii < row:
                    if tip_permutation[ii]==1:
                        cc=cc+1
                    elif tip_permutation[ii]==0:
                        tmp.append(cc)
                        cc=0
                        break
                    ii=ii+1
                    if ii == row:
                        tmp.append(cc)
                        break
                ii=ii+1
            if  tip == tuple(tmp):
                return_all_permutation.append(tip_permutation)
        #print("return_all",return_all_permutation)
        #計算[1,0,1,1,0]->[1,2],[1,0,1,0,1]->[1,1,1],[0,1,1,0,0]->[2]
        if len(return_all_permutation)==1:
            #print("return",list(return_all_permutation[0]))
            return list(return_all_permutation[0])
        return_permutation=[]
        judge_known=list(zip(*return_all_permutation))
        for jk in judge_known:
            for ii in range(len(jk)):
                if ii == len(jk)-1:
                    return_permutation.append(jk[0])
                    break
                elif jk[ii]!=jk[ii+1]:
                    return_permutation.append(-1)
                    break
        #print("return",return_permutation)
        #print(return_permutation)    
        return return_permutation
    def solve(self):
        while not all(map(lambda x:0 if -1 in x else 1,self.NxN)):
            for tip_all in self.clues:
                for rr,tip in enumerate(tip_all):
                    #print("tip:",tip)
                    #print("rr",rr)
                    self.NxN[rr]=self.all_possible(self.NxN[rr],tip,row=5)
                    #print("NxN",self.NxN)
                self.NxN=list(zip(*self.NxN))
                #print("NxN,rr",self.NxN)
        return tuple(zip(*self.NxN))
clues = (((1,), (3,), (1,), (3, 1), (3, 1)),
          ((3,), (2,), (2, 2), (1,), (1, 2)))
