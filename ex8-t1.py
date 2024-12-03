thislist = ["apple", "banana", "cherry"]

print(thislist)

for x in thislist:
  print(x)

print(len(thislist))

for x in range(0,len(thislist)):
    print(x,"  ")
    print(thislist[x])
    
thislist[0]="hello"
print(thislist)


thist = ("apple", "banana", "cherry")

print(thist)

for x in thist:
  print(x)

print(len(thist))

for x in range(0,len(thist)):
    print(x,"  ")
    print(thist[x])

'''
錯誤示範
'''
thislist[0]="hello"
print(thist)
