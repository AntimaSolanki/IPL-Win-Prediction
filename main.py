s=str(input())
x=int(input())
s1=s.upper()
l=list(*s1)
c=0
for i in range(0,len(s1)):
    if (l[i]=='A' or l[i]=='E' or l[i]=='I' or l[i]=='O' or l[i]=='U'):
        c+=1
print(c)