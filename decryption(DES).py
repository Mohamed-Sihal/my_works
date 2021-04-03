def dec_init_per_pt(s):
    per = [57, 49, 41, 33, 25, 17, 9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7,
           56, 48, 40, 32, 24, 16, 8, 0,
           58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6]
    value=len(s)*'0'
    value=list(value)
    
    for i in range(0,len(per)):
        value[per[i]]=s[i]
    t=""    
    for i in value:
        t=t+i
    return t


def sub_box(s):
    r=""
    sbox= [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],  
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],  
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],  
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],  
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],  
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],  
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],  
    
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],  
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],  
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],  
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],  
        
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],  
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],  
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],  
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],  
         
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],  
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],  
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],  
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],  
        
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],  
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],  
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],  
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],  
          
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],  
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],  
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],  
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],  
         
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],  
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],  
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],  
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]
    
    
    
    for i in range(0,8):
        
        t=s[(i*6) : (i*6)+6]
        
        row=str(t[0])+str(t[5])
       
        column=t[1:5]
        
        row=int(row,2)
        column=int(column,2)
        
        value=sbox[i][row][column]
        
        value=bin(int(value)).replace("0b", "")
        value=str(value)
        value=((4-len(value))*'0')+value
        r=r+value
        
    return(r)



def permi(s):
    value=""
    table = [ 16,  7, 20, 21,
           29, 12, 28, 17,  
           1, 15, 23, 26,  
           5, 18, 31, 10,
           2,  8, 24, 14,
           32, 27,  3,  9,  
           19, 13, 30,  6,  
           22, 11,  4, 25 ]
    for i in table:
        value+=s[i-1]
    return value


def init_per_key(s):
    value=""
    table = [57, 49, 41, 33, 25, 17, 9,  
        1, 58, 50, 42, 34, 26, 18,  
        10, 2, 59, 51, 43, 35, 27,  
        19, 11, 3, 60, 52, 44, 36,  
        63, 55, 47, 39, 31, 23, 15,  
        7, 62, 54, 46, 38, 30, 22,  
        14, 6, 61, 53, 45, 37, 29,  
        21, 13, 5, 28, 20, 12, 4 ]
    for i in table:
        value+=s[i-1]
    return value

def exp_per_pt(s):
    value=s[31]+s[0:4]+s[4] 
    for i in range(1,7):
        value=value+s[(i*4)-1] + s[(i*4) : (i*4)+4] + s[(i*4)+4]
    value= value + s[27] + s[28 :] + s[0]
    return(value)


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

def pc2(s):
    value=""
    table = [14, 17, 11, 24, 1, 5,  
            3, 28, 15, 6, 21, 10,  
            23, 19, 12, 4, 26, 8,  
            16, 7, 27, 20, 13, 2,  
            41, 52, 31, 37, 47, 55,  
            30, 40, 51, 45, 33, 48,  
            44, 49, 39, 56, 34, 53,  
            46, 42, 50, 36, 29, 32 ] 
    
    for i in table:
        value+=s[i-1]
    return(value)


def leftshift(s):
    value=s[1:]+s[0]
    return value


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
    return(res[2:100:5])



def inverse_permutation(s):
    value=''
    table = [ 40, 8, 48, 16, 56, 24, 64, 32,  
               39, 7, 47, 15, 55, 23, 63, 31,  
               38, 6, 46, 14, 54, 22, 62, 30,  
               37, 5, 45, 13, 53, 21, 61, 29,  
               36, 4, 44, 12, 52, 20, 60, 28,  
               35, 3, 43, 11, 51, 19, 59, 27,  
               34, 2, 42, 10, 50, 18, 58, 26,  
               33, 1, 41, 9, 49, 17, 57, 25 ]
    value="0"*len(s)
    value=list(value)    
    
    for i in range(len(table)):
        value[table[i]-1]=s[i]
    t=""
    for i in value:
        t=t+str(i)
    
    return t
    '''
    for i in table:
        value+=s[i-1]
    return(value)'''






alpha={'0':"0000",'1':"0001",'2':"0010",'3':"0011",
       '4':"0100",'5':"0101",'6':"0110",'7':"0111",
       '8':"1000",'9':"1001",'A':"1010",'B':"1011",
       'C':"1100",'D':"1101",'E':"1110",'F':"1111"}


plainText='C0B7A8D05F3A829C'#input("Enter the Plain Text :")
key="AABB09182736CCDD"#input("Enter the key :")

if(plainText.islower()):
    plainText=plainText.upper()
if(key.islower()):
    key=key.upper()
constant=0
for i in plainText:
    if((ord(i)>=65)and(ord(i)<=70)):
        constant=1
#if its a value greater than 65
#I'll fill this
#print(plainText)
l1=[]
i=0
while i<len(plainText):
    x=plainText[i]
    i=i+1
    l1.append(alpha[x])
s1=""
i=0
while(i<len(l1)):
    y=str(l1[i])
    s1+=y
    i=i+1
#print(key)
l2=[]
i=0
while i<len(key):
    x=key[i]
    i=i+1
    l2.append(alpha[x])
s2=""
i=0
while(i<len(l2)):
    y=str(l2[i])
    s2+=y
    i=i+1
#print(l1)
key1=s2;


keyvalues=[]

#initial key Permutation
key2=init_per_key(key1)
C0=""
D0=""
C1=""
D1=""



for iii in range(1,17):

    #dividing the C0 and D0
    C0=key2[0:28]
    D0=key2[28:56]
    C1=leftshift(C0)
    D1=leftshift(D0)
    C1=leftshift(C1)
    D1=leftshift(D1)
    if(iii==1 or iii==2 or iii==9 or iii==16):
        
        C1=leftshift(C0)
        D1=leftshift(D0)
    per2_key=""
    per2=""
    per2_key=C1+D1
    
    key2=per2_key
    per2=pc2(per2_key)
   
    keyvalues.append(per2)
    
    key2=per2_key
    
keyvalues=keyvalues[::-1]




inti_text=inverse_permutation(s1)
for i in range(0,16):
    
    

    left=inti_text[0:32]

    right=inti_text[32:]    
    

    #print("l0  " +hexa(left))
    #print("r0  "+hexa(right))

    #print("key "+hexa(keyvalues[i]))
    R0=right

    ex=exp_per_pt(R0)


    kw4=""
    kw4=xor(ex,keyvalues[i])

    kw5=""
    kw5=sub_box(kw4)

    kw6=""
    kw6=permi(kw5)    
    


    l1=xor(kw6,left)
    
    
    
    inti_text=R0+l1
    



inti_text=inti_text[32:64]+inti_text[0:32]

#print(hexa(inti_text))

pt=dec_init_per_pt(inti_text)

print(hexa(pt))


    
    