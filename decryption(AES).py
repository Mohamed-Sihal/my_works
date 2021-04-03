"""
Created on Tue Feb 16 17:22:23 2021
@author: md_rila_
"""
def xor1(s):
    x=""
    x=str(s[0])
    for i in range(len(s)-1,0,-1):
        x=xor(x,s[i])
    return(x)

def mul(s,l):
    x=""
    x=l[int(s[0])]
    for i in range(len(s)-1,0,-1):
        x=xor(x,l[int(s[i])])        
    return(x)

def g_x(l):
    mx=[[['2','3','1'],['0','1','3'],['0','2','3'],['0','3']],
       [['0','3'],['1','2','3'],['0','1','3'],['0','2','3']],
       [['0','2','3'],['0','3'],['1','2','3'],['0','1','3']],
       [['0','1','3'],['0','2','3'],['0','3'],['1','2','3']]]
    l1=[]
    count=0
    x=""
    for i in range(4):
        for j in range(4):
            result=[]
            for k in range(4):
                count+=1
                result.append(mul(mx[i][k],l[k][j]))
            x=xor1(result)
            l1.append(x)
    return(l1)

def list_sep(l):
    s=""
    li=[]
    for i in range(0,len(l)):
        l1=[]
        s=l[i]
        l1.append(s)
        count=0
        while(count<(len(s)-1)):
            if(s[0]=='1'):
                s=leftshift(s)
                s=xor(s,"00011011")
                l1.append(s)
            elif(s[0]=='0'):
                s=leftshift(s)
                l1.append(s)
            count+=1
        li.append(l1)
    return(li)

def leftshift(s):
    value=s[1:]+"0"
    return value

def xor(v1,v2):
    res=""
    i=0
    while(i<len(v1)):
        if(v1[i]==v2[i]):
            res+="0"
        else:
            res+="1"
        i+=1
    return(res)

def alpha(s):
    alphas={'0':"0000",'1':"0001",'2':"0010",'3':"0011",
       '4':"0100",'5':"0101",'6':"0110",'7':"0111",
       '8':"1000",'9':"1001",'A':"1010",'B':"1011",
       'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
    k=0
    x=""
    while k<len(s):
        x+=alphas[s[k]]
        k=k+1    
    return(x)

def mix_col(mat):
    s=""
    i=0
    j=0
    r=len(mat)
    mat_1=""
    l2=[]
    c=len(mat[0])
    for i in range(r):
        for j in range(c):
            s=str(mat[i][j])
            s=alpha(s)
            mat_1+=s
    mat2=[]
    for i in range(0,len(mat_1),8):
        mat2.append(mat_1[i:i+8])
    s1=[]
    s3=[]
    s5=[]
    s1=list_sep(mat2)
    for i in range(0,16,4):
        l2.append(s1[i:i+4])
    s1=g_x(l2)
    for i in range(0,16,1):
        s5.append(hexa(str(s1[i])))
    for i in range(0,16,4):
        s3.append(s5[i:i+4])
    return(s3)

def inv_sbox(s):
    l1=[]
    sbox=['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB',
          '7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB',
          '54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E',
          '08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25',
          '72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92',
          '6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84',
          '90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06',
          'D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B',
          '3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73',
          '96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E',
          '47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B',
          'FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4',
          '1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F',
          '60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF',
          'A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61',
          '17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']
    for i in range(0,len(s),1):
        if(len(s[0])==2):
            row=s[i][0]
            col=s[i][1]
            if(row.isalpha()):
                row=ord(row)-55
            if(col.isalpha()):
                col=ord(col)-55
            n=int(row)*16
            n=n+int(col)
            n=int(n)
            l1.append(sbox[n])
            return l1
        elif(len(s)==2):
            row=s[0]
            col=s[1]
            if(row.isalpha()):
                row=ord(row)-55
            if(col.isalpha()):
                col=ord(col)-55
            n=int(row)*16
            n=n+int(col)
            n=int(n)
            l1.append(sbox[n])
            return l1
        else:
            for j in range(0,len(s[0]),1):
                for k in range(0,1,1):
                    row=s[i][j][0]
                    col=s[i][j][1]
                    if(row.isalpha()):
                        row=ord(row)-55
                    if(col.isalpha()):
                        col=ord(col)-55
                    n=int(row)*16
                    n=n+int(col)
                    n=int(n)
                    l1.append(sbox[n])
            return l1
def sbox(s):
    l1=[]
    sbox=['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB',
   '76', 'CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4',
   '72', 'C0', 'B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71',
   'D8', '31', '15', '04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2',
   'EB', '27', 'B2', '75', '09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6',
   'B3', '29', 'E3', '2F', '84', '53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB',
   'BE', '39', '4A', '4C', '58', 'CF', 'D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45',
   'F9', '02', '7F', '50', '3C', '9F', 'A8', '51', 'A3', '40', '8F', '92', '9D', '38', 'F5',
   'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2', 'CD', '0C', '13', 'EC', '5F', '97', '44',
   '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73', '60', '81', '4F', 'DC', '22', '2A',
   '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB', 'E0', '32', '3A', '0A', '49',
   '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79', 'E7', 'C8', '37', '6D',
   '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08', 'BA', '78', '25',
   '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A', '70', '3E',
   'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E', 'E1',
   'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF',
   '8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
    for i in range(0,len(s),1):
        if(len(s[0])==2):
            row=s[i][0]
            col=s[i][1]
            if(row.isalpha()):
                row=ord(row)-55
            if(col.isalpha()):
                col=ord(col)-55
            n=int(row)*16
            n=n+int(col)
            n=int(n)
            l1.append(sbox[n])
            return l1
        elif(len(s)==2):
            row=s[0]
            col=s[1]
            if(row.isalpha()):
                row=ord(row)-55
            if(col.isalpha()):
                col=ord(col)-55
            n=int(row)*16
            n=n+int(col)
            n=int(n)
            l1.append(sbox[n])
            return l1
        else:
            for j in range(0,len(s[0]),1):
                for k in range(0,1,1):
                    row=s[i][j][0]
                    col=s[i][j][1]
                    if(row.isalpha()):
                        row=ord(row)-55
                    if(col.isalpha()):
                        col=ord(col)-55
                    n=int(row)*16
                    n=n+int(col)
                    n=int(n)
                    l1.append(sbox[n])
            return l1

rconst=['00000001000000000000000000000000',
        '00000010000000000000000000000000',
        '00000100000000000000000000000000',
        '00001000000000000000000000000000',
        '00010000000000000000000000000000',
        '00100000000000000000000000000000',
        '01000000000000000000000000000000',
        '10000000000000000000000000000000',
        '00011011000000000000000000000000', 
        '00110110000000000000000000000000', 
        '01101100000000000000000000000000', 
        '11011000000000000000000000000000', 
        '10101011000000000000000000000000', 
        '01001101000000000000000000000000']

def hexa(s):
    res=""
    k=""
    x=""
    alpha={'0':"0000",'1':"0001",'2':"0010",'3':"0011",
    '4':"0100",'5':"0101",'6':"0110",'7':"0111",
    '8':"1000",'9':"1001",'A':"1010",'B':"1011",
    'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
    for i in range(0,len(s),4):
        k=s[i:i+4]
        x=[number for number,name in alpha.items() if name==k]
        res+=str(x)
    return(res[2:1000:5])

def binary(s):
    alpha={'0':"0000",'1':"0001",'2':"0010",'3':"0011",
       '4':"0100",'5':"0101",'6':"0110",'7':"0111",
       '8':"1000",'9':"1001",'A':"1010",'B':"1011",
       'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
    x=""
    if(len(s)!=1):
        for i in range(0,len(s),1):
            x+=alpha[s[i]]
        return x
    else:
        return(alpha[s])

def rot_word(s):
    value=s[2:]+s[0:2]
    return value

def t_gen(s):
    y=""
    x=""
    x=hexa(s)
    x=rot_word(x)
    l1=[]
    for i in range(0,len(x),2):
        l1.append(x[i:i+2])
    x=[]
    for i in range(0,len(l1),1):
        x.append(sbox(l1[i]))
    for i in range(0,len(x),1):
        y+=binary(x[i][0])
    return(y)

def key_gen(l):
    w=[]
    count=0
    gen_keys=[]
    s=""
    for i in range(0,len(l),1):
        for j in range(0,len(l[0]),1):
            s+=binary(l[i][j])
    gen_keys.append(s)
    for i in range(0,len(s),32):
        w.append(s[i:i+32])  
    for i in range(4,44,1):
        t=""
        if(i%4!=0):
            w.append(xor(w[i-1],w[i-4]))
        elif(i%4==0):
            t=t_gen(w[i-1])
            t=xor(t,rconst[count])
            w.append(xor(t,w[i-4]))
            count+=1
    x=""
    for i in range(4,len(w),1):
        if((i%4==0)and(i!=4)):
            gen_keys.append(x)        
            x=""
        x+=w[i]
        if(i==len(w)-1):
            gen_keys.append(x)
    return gen_keys

def left_shift_row(s):
    l1=[]
    l1.append(s[3])
    for i in range(0,3,1):
        l1.append(s[i])
    return l1

def shift_row(s):
    for i in range(1,len(s),1):
        count=0
        while(count<i):
            s[i]=left_shift_row(s[i])
            count+=1
    return s

def state_conv(s):
    alpha={'A':"00",'B':"01",'C':"02",'D':"03",
       'E':"04",'F':"05",'G':"06",'H':"07",
       'I':"08",'J':"09",'K':"0A",'L':"0B",
       'M':"0C",'N':"0D",'O':"0E",'P':"0F",
       'Q':"10",'R':"11",'S':"12",'T':"13",
       'U':"14",'V':"15",'W':"16",'X':"17",
       'Y':"18",'Z':"19"}
    l=[]
    s1=""
    if((len(s)!=16)):
        for i in range(len(s),16,1):
            s+='Z'
    l=list(s)
    for i in range(0,len(l),1):
        if(l[i].islower()):
            l[i]=l[i].upper()
        s1+=l[i]
    s=[]
    i=0
    while i<len(s1):
        x=s1[i]
        i=i+1
        s.append(alpha[x])
    s1=[]
    for i in range(0,16,4):
        s1.append(s[i:i+4])
    return s1
"""pt=input("Enter the plain text")
key=input("Enter the key")
pt=state_conv(pt)
key=state_conv(key)"""
key=[['54', '68', '61', '74'],
    ['73', '20', '6D', '79'],
    ['20', '4B', '75', '6E'],
    ['67', '20', '46', '75']]
key=key_gen(key)
pt=[['29', 'C3', '50', '5F'], ['57', '14', '20', 'F6'], ['40', '22', '99', 'B3'], ['1A', '02', 'D7', '3A']]
l1=[]
y=""
for i in range(0,len(pt),1):
    for j in range(0,len(pt[0]),1):
        y+=binary(pt[i][j])
pt=y
text=xor(pt,key[10])
y=[]
j=0
x=[]
for i in range(0,len(text),8):
    y.append(hexa(text[i:i+8]))
text=[]
for i in range(0,len(y),4):
    text.append(y[i:i+4])
zero=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(0,len(text),1):
    for j in range(0,len(text[0]),1):
        zero[i][j]=text[j][i]
text=zero
for times in range(9,-1,-1):
    text=shift_row(text)
    x=[]
    y=[]
    for i in range(0,len(text),1):
        for j in range(0,len(text[0]),1):
            x.append(inv_sbox(text[i][j]))
    for i in range(0,len(x),1):
        y.append(x[i][0])
    x=[]
    for i in range(0,len(y),4):
        x.append(y[i:i+4])
    text=x
    print("After Sbox")
    print(text)
    y=""
    for i in range(0,len(text),1):
        for j in range(0,len(text[0]),1):
            y+=binary(text[i][j])
    text=y
    y=[]
    zen=key[times]
    for i in range(0,len(zen),8):
        y.append(hexa(zen[i:i+8]))
    text1=[]
    for i in range(0,len(y),4):
        text1.append(y[i:i+4])
    zero=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0,len(text1),1):
        for j in range(0,len(text1[0]),1):
            zero[i][j]=text1[j][i]
    text1=zero
    y=""
    for i in range(0,len(text1),1):
        for j in range(0,len(text1[0]),1):
            y+=binary(text1[i][j])
    text1=y
    text=xor(text,text1)
    print("After add round key")
    print(hexa(text))
    y=[]
    for i in range(0,len(text),8):
        y.append(hexa(text[i:i+8]))
    text=[]
    for i in range(0,len(y),4):
        text.append(y[i:i+4])
    if(times!=0):
        text=mix_col(text)
    print("After inevrse mix col")
    print(text)
zero=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(0,len(text),1):
    for j in range(0,len(text[0]),1):
        zero[i][j]=text[j][i]
text=zero
print("The Plain text is")
for i in range(0,len(text),1):
    for j in range(0,len(text[0]),1):                   
        print("",text[i][j],end="")