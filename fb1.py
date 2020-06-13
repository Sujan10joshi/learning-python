ch=""
rg=30

for j in range(1,rg):
    if j==1:
        ch=ch + str(j) + ch[::-1]
    else:
        if len(ch)%2==0:
            end=len(ch)//2
        else:
            end=len(ch)//2+1
        ch=ch[:end] + str(j) + (ch[:end])[::-1]
    print(ch.center(rg*2))