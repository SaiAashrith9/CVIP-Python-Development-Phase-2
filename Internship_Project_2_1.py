import time
import sys
import nltk
import random
import tkinter as tk
from timeit import default_timer as timer 
from nltk.corpus import treebank
#nltk.download('treebank')




from nltk.corpus import treebank

from nltk.tokenize.treebank import TreebankWordTokenizer


from nltk.tokenize.treebank import TreebankWordDetokenizer


#print(treebank.fileids()[:10])


twd=TreebankWordDetokenizer()
r=random.randint(1,2)
print('\n---------\nPRESS ANY ALPHANUMERIC KEY TO BEGIN:')
sys.stdin.read(1)
print('\n---------\nHERE IS THE TEXT :)')
if r==1:
    a=treebank.words('wsj_0009.mrg')


    print(twd.detokenize(a),end='\n---------\n')

else:
    a=treebank.words('wsj_0018.mrg')
    
    print(twd.detokenize(a),end='\n---------\n')

print('PLEASE TYPE THE TEXT GIVEN ABOVE:-\n')
t=timer()
#print(t)
i=sys.stdin.read(1)
sys.stdin.flush()
while (True):
    if timer()<t+60:
        i+=sys.stdin.read(1)
        sys.stdin.flush()
    else:    
        break

print('---------\nTHE TEXT ENTERED IS AS FOLLOWS:-\n')
    
print(i)    
count=0
actual_tokens=a     #TreebankWordTokenizer().tokenize(a)
typed_tokens=TreebankWordTokenizer().tokenize(i)

c=[]
print('\n---------\nTOKENS:-\n\n<--->Entered text---Given text\n')
if i==a:
    count=len(i)
else:
    for i in range(len(typed_tokens)):
        for j in range(len(actual_tokens)):
            b=0
            print(typed_tokens[i],end=f'---{actual_tokens[j]}\n')
            #c[i]=False
            for a in c:
                if a[0]==i or a[1]==j:
                    b=1
                    break
            if b==1:
                continue
            else:
                if typed_tokens[i]==actual_tokens[j]: 
                    c.append((i,j))
                    count+=1
print('\n---------\nINDICES WHERE TOKENS ARE MATCHED:-\n\n<--->(Entered text,Given text)\n')
print(c)
        
print(f'\n---------\n\nNUMBER OF WORDS GIVEN:{len(actual_tokens)}\nNUMBER OF WORDS TYPED:{len(typed_tokens)}\nNUMBER OF WORDS TYPED CORRECTLY :{count}')
print('\n---------\nNOTE:The numbers might not be completely accurate ; but they do give you an approximate idea of your typing speed')