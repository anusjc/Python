def solve():
    m=int(input())
    l=[]
    lo=[]
    for x in range(1,m**2+1):
        if(x%2==0):
            l.append(x)
        else:
            lo.append(x) 
    a=0
    b=0
    for i in range(m):
        for j in range(m):
            if((i+j)%2==0):
                print(lo[a],end=' ')
                a+=1           
            else:
                print(la[b],end=' ')
                b+=1  

    print()
for _ in range(int(input())):
    solve()
                                
