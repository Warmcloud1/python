#輸入2個人的勝率，先手放前面
def Versus(a,b):
    c=(1-a)*b*(1/(1-(1-a)*(1-b)))
    c=1-c
    #print("先手的勝率",c,"\n後手的勝率",1-c)
    return c
me=0.6
b=0.6
c=0.7
ans=0.6*(1-Versus(0.7,me))+0.4*0.7*Versus(me,0.7)+0.4*0.3*0.9*Versus(me,0.9)
def Vs3(a,b,c):
    #第一回合a開始
    if a>b>c:
        a*(1-Verse(c,a))
    pass

class Wizard():
    def __init__(self,winrate):
        self.winrate=winrate
        
    #死亡 -1
    def death(self):
        self.winrate=-1

    #選擇 打高趴數的   
    def choose(self):
        pass


