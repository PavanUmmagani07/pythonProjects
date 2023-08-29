N = int(input())
for i in range(1,N+1):
    left_Spaces = (N-i)*" "
    hollow_Spaces = (i-2)*"  "
    if(i==1):
        print(left_Spaces+"*")
    else:
        print(left_Spaces+"* "+hollow_Spaces+"*")

for j in range(N,0,-1):
    left_Spaces = (N-j)*" "
    hollow_Spaces = (j-2)*"  "
    if(j==1):
        print(left_Spaces+"*")
    else:
        print(left_Spaces+"* "+hollow_Spaces+"*")



N = int(input())
for i in range(1,N+1):
    left_Spaces = (N-i)*" "
    hollow_Spaces = (i-2)*"  "
    if(i == 1):
        print(left_Spaces+"*")
    else:
        print(left_Spaces+"* "+hollow_Spaces+"*")

for j in range(1,N):
    left_Spaces = j*" "
    hollow_Spaces = (N-(j+1))*"  "
    if(j==N):
        print(left_Spaces+"*")
    else:
        print(left_Spaces+"* "+hollow_Spaces+"*")



