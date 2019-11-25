'''
困難點:把變數值變成變數EX:a='b'，用a表示 'b'= 某值
學習點: 1."12"isnumber
        2.for 迴圈回到前一個迴圈值，解決用while
        3.字典應用:增加 尋找 dict={key1:value1,key2:value2} EX:dict1.setdefault(words[1],int(words[2]))
'''
def is_number(s):
        try:
                float(s)
                return True
        except ValueError:
                return False


def simple_assembler(program):
        dict1={}
        nn=0
        while nn < len(program):
                words=program[nn].split()
                if words[0]=="mov":
                        #words[1]未記錄
                        if words[1] not in dict1.keys():
                                if is_number(words[2]):
                                        dict1.setdefault(words[1],int(words[2]))
                                else:
                                        dict1.setdefault(words[1],dict1[words[2]])
                                        print(dict1)
                        #words[1]已記錄
                        else:
                                if is_number(words[2]):
                                        dict1[words[1]]=int(words[2])     
                                else:
                                        dict1[words[1]]=dict1[words[2]]
                elif words[0]=="inc":
                        if str(words[1]) not in dict1.keys():
                                print("no definee varable")
                        else:
                                dict1[words[1]]=dict1[words[1]]+1
                elif words[0]=="dec":
                        if str(words[1]) not in dict1.keys():
                                print("no definee varable")
                        else:
                                dict1[words[1]]=dict1[words[1]]-1
                elif words[0]=="jnz":
                        
                        if is_number(words[1]):
                                nn+=int(words[2])
                                continue

                        elif dict1[words[1]]==0:
                                nn += 1
                                continue
                        else:
                                nn += int(words[2])
                                continue
                nn += 1
        #print(program)
        return (dict1)
code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
a=code.splitlines()
simple_assembler(a)
program=['mov a 1','mov b 1','mov c 0','mov d 26','jnz c 2','jnz 1 5','mov c 7','inc d','dec c','jnz c -2','mov c a','inc a','dec b','jnz b -2','mov b c','dec d','jnz d -6','mov c 18','mov d 11','inc a','dec d','jnz d -2','dec c','jnz c -5']
#simple_assembler(program)



def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        cmd, r, v = (program[i] + ' 0').split()[:3]
        if cmd == 'inc': d[r] += 1
        if cmd == 'dec': d[r] -= 1        
        if cmd == 'mov': d[r] = d[v] if v in d else int(v)
        if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
        i += 1
    return d
