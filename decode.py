print("\033c\033[47;31m\ngive me a binary 16 bits .bin file to decript ? ")
a=input().strip()
b=a.replace(".bin","")
print("\033[47;31m\ngive me a password to encript ? ")
c=input().strip()
f1=open(a,"rb")
f=f1.read()
f1.close()
r=b''
counter=0
counter1=0
g=c.encode()
z1=0
z2=0
for ff in f:
   if counter1==0:
       i=int(ff)
       z1=i
       
       
       
   if counter1==1:
       i=int(ff)
       i=i*256+z1
       ii=int(g[counter])
       fff=0xff & (i+ii)
       rr=bytearray([fff])
       
       r=r+rr
       counter=counter+1
       if counter>=len(g):
           counter=0

   counter1=(counter1+1)& 1
f1=open(b+".txt","bw")
f1.write(r)
f1.close()