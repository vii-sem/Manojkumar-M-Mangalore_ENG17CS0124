fname=input('Enter file:')
if len(fname) < 1 :fname='C:/Users/Varnith GV/Desktop/DSU/7th Semester/Web Programming Lab/Programs/steps.txt'

hand=open(fname)
di=dict()
for lin in hand:
    for ch in lin:
            if ch in "~@#$%^&*()_-+=<>?/.,:;!{}[]''": 
                lin=lin.replace(ch," ")
                
    lin=lin.rstrip()
    #print(lin)
    wds=lin.split() 
   

   

    for w in wds:
        di[w]=di.get(w,0)+1
    largest=-1
    theword=None
    for k,v in di.items():  
    
        if v>largest:
            largest=v
            theword=k
print("the most frequent word found is")
print(theword,largest)

    

        
       



