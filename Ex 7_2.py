n =5
x = n*[0]
c1 =0
c0 =0
c_1 =0

for i in range(0,3):
    x[i] = int(input())
    if x[1] > 0:
        print("x[i] > 0 ")
        c1+=1
    elif x[i] < 0 :
        print("x[i]< 0 ")
        c_1=c_1+1
    else:
        print("x[i] == 0 ")
        c0=c0+1    
    print("i= ",x[i])
print(">0: ",c1)
print("==0 ",c0)
print("i<0 ",c_1
