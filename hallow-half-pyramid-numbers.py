R=int(input())
for i in range(1,R+1):
  for j in range(i,R):
    print(" ",end="")
  for j in range(1,i+1):
    if i==R or j==1 or j==i:
      if j==i:
        print(j,end="")
      else:
        print(j,end=" ")
    else:
      print(" ",end=" ")
  print()
