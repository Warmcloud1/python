'''將ab檔資料做整理成3種 皆有ab存在、只存在a的、只存在b的'''

import csv
import pandas as pd
import numpy as np
import time
input_file1="a.csv"
input_file2="b.csv"
write_data=''
result_title =[]
result_titlea=[]
result_titleb=[]
same=[]
diffa=[]
diffb=[]
IDb=[]
#read two files
file1=pd.read_csv(input_file1,encoding='utf8')
file2=pd.read_csv(input_file2,encoding='utf8')
with open(input_file1,'r',newline = '',encoding='utf8') as filex1:
    filereadera=csv.reader(filex1)
    headera=next(filereadera)
#counting header and write geadercontent
titlea =[n for n in headera if n!='']
titlea[0]=titlea[0].strip('\ufeff')
count_headera=len(titlea)
with open(input_file2,'r',newline = '',encoding='utf8') as filex2:
    filereaderb=csv.reader(filex2)
    headerb=next(filereaderb)
#counting header and write geadercontent
titleb =[n for n in headerb if n!='']
titleb[0]=titleb[0].strip('\ufeff')
count_headerb=len(titleb)
l_a=len(file1[titlea[0]])
l_b=len(file2[titleb[0]])
count_a=0
count_b=0

#diffb檔案的title
for b in titleb:
    result_titleb.append(b)
diffb.append(result_titleb)
#a跟b title若重複,刪除重複者
for a in titlea:
    n=0
    for b in titleb:
        if a==b:
            del titleb[n]
        n += 1
#ab相同檔案title,diffa檔案title
for a in titlea:
    result_title.append(a)
    result_titlea.append(a)
diffa.append(result_titlea)
for b in titleb:
    if b=='身分證號'or b=='身分證' or b =='身份證' or b=='身份證號' or b=='id' or b=='身分證字號' or b=='身份證字號':
        pass
    else:
        result_title.append(b)
for a in titlea:
    if a=='身分證號'or a=='身分證' or a =='身份證' or a=='身份證號' or a=='id' or a=='身分證字號' or a=='身份證字號':
        IDa =[content for content in file1[a]]
        break
    count_a+=1
for b in result_titleb:
    if b=='身分證號'or b=='身分證' or b =='身份證' or b=='身份證號' or b=='id' or b=='身分證字號' or b=='身份證字號':
        IDb =[content for content in file2[b]]
        break
    count_b+=1
same.append(result_title)
count_ac=0
for a in IDa:
    count_bc=0
    same_temp=[]
    diff_temp=[]
    for b in IDb:
        if a==b:
            for ta in titlea:
                if type(file1[ta][count_ac])!= str and np.isnan(float(file1[ta][count_ac])):
                    same_temp.append('none')
                else:
                    same_temp.append(str(file1[ta][count_ac]))
            bc=0
            for tb in titleb:
                if type(file2[tb][count_bc]) != str and np.isnan(float(file2[tb][count_bc])):
                    same_temp.append('none')
                else:
                    same_temp.append(str(file2[tb][count_bc]))
                bc += 1
            same.append(same_temp)
            break
        elif a!=b and count_bc+1 ==l_b:
            for ta in titlea:
                diff_temp.append(str(file1[ta][count_ac]))
            diffa.append(diff_temp)
        count_bc += 1
    count_ac += 1
count_bc = 0
for b in IDb:
    count_ac =0
    same_temp=[]
    diff_temp=[]
    for a in IDa:
        if a==b:
            break
        elif a!=b and count_ac+1 ==l_a:
            for tb in result_titleb:
                diff_temp.append(str(file2[tb][count_bc]))
            diffb.append(diff_temp)
        count_ac +=1
    count_bc += 1
#same diffa diffb 
with open('ab檔案皆存在者.csv','w',newline='',encoding='utf8') as file:
    filewriter=csv.writer(file)
    #filewriter.writerow(write_title(filename))
    for row in same:
        filewriter.writerow(row)
with open('僅存在a檔案者.csv','w',newline='',encoding='utf8') as file2:
    filewriter=csv.writer(file2)
    #filewriter.writerow(write_title(filename))
    for row in diffa:
        filewriter.writerow(row)
with open('僅存在b檔案者.csv','w',newline='',encoding='utf8') as file3:
    filewriter=csv.writer(file3)
    #filewriter.writerow(write_title(filename))
    for row in diffb:
        filewriter.writerow(row)
print('感謝seafood 讚嘆seafood')
time.sleep(3)
