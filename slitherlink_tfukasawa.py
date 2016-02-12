#スリザーリンク4*4のmaster
N=4
M=4
col=[[1 for i in range(N)] for j in range(M+1)]
row=[[1 for i in range(N+1)] for j in range(M)]

def link(s,t):
    if s<N and t<M:
        c=col[s][t]+col[s][t-1]+row[s][t]+row[s-1][t]
    elif s==N and t!=M:
        c=col[s][t]+col[s][t-1]+row[s-1][t]
    elif s!=N and t==M:
        c=col[s][t-1]+row[s][t]+row[s-1][t]
    else:
        c=col[s][t-1]+row[s-1][t]
    
    if c==0 or c==2:
        return True
    else:
        return False
        
def allink(s,t):
    for i in range(s):
        for j in range(t):
            if link(i,j)==False:
                return False

def solved(a):
    if a==None:
        print(col)
        print(row)
    else:
        print("unsolved")

solved(allink(N+1,M+1))
ten=[[x,y]for y in range(5) for x in range(5)]

def tenten(x,y):
    return ten [(5*y)+x]

newten=[]
def draw():
    for n in range(2):
        if x==0 and y==0 :
            newten.append(tenten(x+(1-n),y+n))
        if x==4 and y==0 :
            newten.append(tenten(x-(1*n),y+(1-n)))
        if x==0 and y==4 :
            newten.append(tenten(x+(1-n),y-(1*n)))
        if x==4 and y==4 :
            newten.append(tenten(x-n,y+(n-1)))
    
    
